import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import json
import os

DATA_PATH = "data/cars.json"
IMG_PATH = "img/"

class Car:
    def __init__(self, model, price, acceleration, car_type, image):
        self.model = model
        self.price = price
        self.acceleration = acceleration
        self.car_type = car_type
        self.image = image

    def value_score(self):
        return self.acceleration / self.price if self.price else float('inf')

class CarManager:
    def __init__(self):
        self.cars = []

    def load_from_json(self, path):
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
            self.cars = [
                Car(item["model"], item["price"], item["acceleration"], item["type"], item["image"])
                for item in data
            ]

    def get_filtered(self, car_type=None, max_price=None, max_acceleration=None):
        filtered = self.cars
        if car_type:
            car_type = car_type.lower()
            filtered = [car for car in filtered if car_type in car.car_type.lower()]
        if max_price:
            filtered = [car for car in filtered if car.price <= max_price]
        if max_acceleration:
            filtered = [car for car in filtered if car.acceleration <= max_acceleration]
        return filtered

    def get_best_value_car(self):
        return min(self.cars, key=lambda car: car.value_score(), default=None)

class CarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Výběr vozu")
        self.manager = CarManager()
        self.manager.load_from_json(DATA_PATH)
        self.create_widgets()

    def create_widgets(self):
        self.filter_frame = tk.LabelFrame(self.root, text="Filtr")
        self.filter_frame.pack(fill="x", padx=10, pady=5)

        tk.Label(self.filter_frame, text="Typ:").grid(row=0, column=0)
        self.type_entry = tk.Entry(self.filter_frame)
        self.type_entry.grid(row=0, column=1)

        tk.Label(self.filter_frame, text="Max Cena:").grid(row=0, column=2)
        self.price_entry = tk.Entry(self.filter_frame)
        self.price_entry.grid(row=0, column=3)

        tk.Label(self.filter_frame, text="Max Zrychlení:").grid(row=0, column=4)
        self.acc_entry = tk.Entry(self.filter_frame)
        self.acc_entry.grid(row=0, column=5)

        tk.Button(self.filter_frame, text="Filtrovat", command=self.filter_cars).grid(row=0, column=6, padx=5)
        tk.Button(self.filter_frame, text="Nejvýhodnější vůz", command=self.show_best_value).grid(row=0, column=7)

        self.tree = ttk.Treeview(self.root, columns=("model", "price", "acceleration", "type"), show="headings")
        for col in ("model", "price", "acceleration", "type"):
            self.tree.heading(col, text=col.title())
            self.tree.column(col, width=100)
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        self.tree.pack(fill="both", expand=True, padx=10, pady=5)

        self.detail_frame = tk.LabelFrame(self.root, text="Detail vozu")
        self.detail_frame.pack(fill="x", padx=10, pady=5)
        self.detail_label = tk.Label(self.detail_frame, text="Vyberte vůz...", anchor="w", justify="left")
        self.detail_label.pack(side="left", fill="both", expand=True)
        self.image_label = tk.Label(self.detail_frame)
        self.image_label.pack(side="right")

        self.load_cars(self.manager.cars)

    def load_cars(self, cars):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for car in cars:
            self.tree.insert("", "end", values=(car.model, car.price, car.acceleration, car.car_type))

    def on_tree_select(self, event):
        selected = self.tree.focus()
        if not selected:
            return
        values = self.tree.item(selected, "values")
        model = values[0]
        car = next((c for c in self.manager.cars if c.model == model), None)
        if car:
            self.detail_label.config(text=f"Model: {car.model}\nCena: {car.price} Kč\nZrychlení: {car.acceleration} s\nTyp: {car.car_type}")
            self.show_image(car.image)

    def show_image(self, image_name):
        try:
            path = os.path.join(IMG_PATH, image_name)
            img = Image.open(path)
            img.thumbnail((200, 200))
            self.tk_img = ImageTk.PhotoImage(img)
            self.image_label.config(image=self.tk_img)
        except Exception as e:
            self.image_label.config(image="", text="Obrázek nelze načíst")

    def filter_cars(self):
        car_type = self.type_entry.get()
        max_price = self.try_parse_int(self.price_entry.get())
        max_acc = self.try_parse_float(self.acc_entry.get())
        filtered = self.manager.get_filtered(car_type, max_price, max_acc)
        self.load_cars(filtered)

    def show_best_value(self):
        car = self.manager.get_best_value_car()
        if car:
            self.load_cars([car])
            self.detail_label.config(text=f"Nejvýhodnější vůz:\nModel: {car.model}\nCena: {car.price} Kč\nZrychlení: {car.acceleration} s\nTyp: {car.car_type}")
            self.show_image(car.image)

    def try_parse_int(self, value):
        try:
            return int(value)
        except:
            return None

    def try_parse_float(self, value):
        try:
            return float(value)
        except:
            return None

if __name__ == "__main__":
    root = tk.Tk()
    app = CarApp(root)
    root.mainloop()