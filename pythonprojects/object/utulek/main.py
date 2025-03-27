import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont


class Animal:
    def __init__(self, name, species, sound, description, vaccinated):
        self.name = name
        self.species = species
        self.sound = sound
        self.description = description
        self.vaccinated = vaccinated

    def make_sound(self):
        return self.sound

    def describe(self):
        return self.description


def animal_info(animal):
    vaccinated_text = "Ano" if animal.vaccinated else "Ne"
    messagebox.showinfo("Info o zvířeti",
                        f"Jméno: {animal.name}\nDruh: {animal.species}\nZvuk: {animal.make_sound()}\nPopis: {animal.describe()}\nOčkovaný: {vaccinated_text}")


class UtulekApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Útulek pro zvířata")

        #--styles--
        heading_one = tkFont.Font(family="Montserrat", size=28, weight="bold")

        tk.Label(root, text="Vítejte v útulku!", font=heading_one).pack(pady=10)

        self.animals = []

        tk.Button(root, text="Přidat zvíře", command=self.add_animal, width=50, height=2, bg="#fafafa").pack(pady=5)
        self.animals_frame = tk.Frame(root, height=50)
        self.animals_frame.pack(padx=10, pady=10)

        self.update_animal_buttons()

    def add_animal(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Přidat zvíře")

        tk.Label(add_window, text="Jméno:").grid(row=0, column=0)
        name_entry = tk.Entry(add_window)
        name_entry.grid(row=0, column=1)

        tk.Label(add_window, text="Druh:").grid(row=1, column=0)
        species_entry = tk.Entry(add_window)
        species_entry.grid(row=1, column=1)

        tk.Label(add_window, text="Zvuk:").grid(row=2, column=0)
        sound_entry = tk.Entry(add_window)
        sound_entry.grid(row=2, column=1)

        tk.Label(add_window, text="Popis:").grid(row=3, column=0)
        description_entry = tk.Entry(add_window)
        description_entry.grid(row=3, column=1)

        tk.Label(add_window, text="Očkovaný:").grid(row=4, column=0)
        vaccinated_var = tk.BooleanVar()
        vaccinated_check = tk.Checkbutton(add_window, text="Ano", variable=vaccinated_var)
        vaccinated_check.grid(row=4, column=1)

        def save_animal():
            name = name_entry.get()
            species = species_entry.get()
            sound = sound_entry.get()
            description = description_entry.get()
            vaccinated = vaccinated_var.get()
            if name and species and sound and description:
                self.animals.append(Animal(name, species, sound, description, vaccinated))
                self.update_animal_buttons()
                add_window.destroy()
            else:
                messagebox.showwarning("Chyba", "Vyplňte všechna pole!")

        tk.Button(add_window, text="Uložit", command=save_animal).grid(row=5, columnspan=2, pady=10)

    def update_animal_buttons(self):
        for widget in self.animals_frame.winfo_children():
            widget.destroy()

        for animal in self.animals:
            tk.Button(self.animals_frame, width=100, height=5, bg="#d1e0d1",text=animal.name, command=lambda a=animal: animal_info(a)).pack(pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = UtulekApp(root)
    root.mainloop()