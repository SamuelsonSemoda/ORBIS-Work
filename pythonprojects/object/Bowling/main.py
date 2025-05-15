import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import json
import os

DATA_PATH = "data/balls.json"
IMG_PATH = "img/"

class Ball:
    def __init__(self, model, price, ball_type, company, weight, core, image, pba_player):
        self.model = model
        self.price = price
        self.ball_type = ball_type
        self.company = company
        self.weight = weight
        self.core = core
        self.image = image
        self.pba_player = pba_player

    def value_score(self):
        return self.weight / self.price if self.price else float('inf')

class BallManager:
    def __init__(self):
        self.balls = []

    def load_from_json(self, path):
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
            self.balls = [
                Ball(
                    item["model"],
                    item["price"],
                    item["type"],
                    item["company"],
                    item["weight"],
                    item["core"],
                    item["image"],
                    item["pba_player"]
                )
                for item in data
            ]

    def get_filtered(self, ball_type=None, max_price=None, max_weight=None):
        filtered = self.balls
        if ball_type:
            ball_type = ball_type.lower()
            filtered = [ball for ball in filtered if ball_type in ball.ball_type.lower()]
        if max_price is not None:
            filtered = [ball for ball in filtered if ball.price <= max_price]
        if max_weight is not None:
            filtered = [ball for ball in filtered if ball.weight <= max_weight]
        return filtered

    def get_best_value_ball(self):
        return min(self.balls, key=lambda ball: ball.value_score(), default=None)

class BallApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Výběr bowlingové koule")
        self.manager = BallManager()
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

        tk.Label(self.filter_frame, text="Max Váha:").grid(row=0, column=4)
        self.weight_entry = tk.Entry(self.filter_frame)
        self.weight_entry.grid(row=0, column=5)

        tk.Button(self.filter_frame, text="Filtrovat", command=self.filter_balls).grid(row=0, column=6, padx=5)
        tk.Button(self.filter_frame, text="Nejvýhodnější koule", command=self.show_best_value).grid(row=0, column=7)

        self.tree = ttk.Treeview(self.root, columns=("model", "price", "type", "company", "weight", "core"), show="headings")
        for col in ("model", "price", "type", "company", "weight", "core"):
            self.tree.heading(col, text=col.title())
            self.tree.column(col, width=100)
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        self.tree.pack(fill="both", expand=True, padx=10, pady=5)

        self.detail_frame = tk.LabelFrame(self.root, text="Detail koule")
        self.detail_frame.pack(fill="x", padx=10, pady=5)
        self.detail_label = tk.Label(self.detail_frame, text="Vyberte kouli...", anchor="w", justify="left")
        self.detail_label.pack(side="left", fill="both", expand=True)
        self.image_label = tk.Label(self.detail_frame)
        self.image_label.pack(side="right")

        self.load_balls(self.manager.balls)

    def load_balls(self, balls):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for ball in balls:
            self.tree.insert("", "end", values=(ball.model, ball.price, ball.ball_type, ball.company, ball.weight, ball.core))

    def on_tree_select(self, event):
        selected = self.tree.focus()
        if not selected:
            return
        values = self.tree.item(selected, "values")
        model = values[0]
        ball = next((b for b in self.manager.balls if b.model == model), None)
        if ball:
            self.detail_label.config(text=f"Model: {ball.model}\nCena: {ball.price} Kč\nTyp: {ball.ball_type}\nFirma: {ball.company}\nVáha: {ball.weight} lbs\nJádro: {ball.core}\nPBA Hráč: {ball.pba_player}")
            self.show_image(ball.image)

    def show_image(self, image_name):
        try:
            path = os.path.join(IMG_PATH, image_name)
            img = Image.open(path)
            img.thumbnail((200, 200))
            self.tk_img = ImageTk.PhotoImage(img)
            self.image_label.config(image=self.tk_img)
        except Exception as e:
            self.image_label.config(image="", text="Obrázek nelze načíst")

    def filter_balls(self):
        ball_type = self.type_entry.get()
        max_price = self.try_parse_int(self.price_entry.get())
        max_weight = self.try_parse_float(self.weight_entry.get())
        filtered = self.manager.get_filtered(ball_type, max_price, max_weight)
        self.load_balls(filtered)

    def show_best_value(self):
        ball = self.manager.get_best_value_ball()
        if ball:
            self.load_balls([ball])
            self.detail_label.config(text=f"Nejvýhodnější koule:\nModel: {ball.model}\nCena: {ball.price} Kč\nTyp: {ball.ball_type}\nFirma: {ball.company}\nVáha: {ball.weight} lbs\nJádro: {ball.core}\nPBA Hráč: {ball.pba_player}")
            self.show_image(ball.image)

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
    app = BallApp(root)
    root.mainloop()