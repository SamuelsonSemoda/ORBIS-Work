import tkinter as tk
from tkinter import messagebox


class Animal:
    def make_sound(self):
        raise NotImplementedError("Podtridy musi byt obsazeny!")

    def describe(self):
        return "Tohle je zvire"


class Dog(Animal):
    def make_sound(self):
        return "Haf!"

    def describe(self):
            return "Pes je čtyřnohé domestikované zvíře, které je známé svou věrností a inteligencí."


class Cat(Animal):
    def make_sound(self):
        return "Mnau!"

    def describe(self):
        return "Kočka je čtyřnohé domestikované zvíře, které je známé svou bystrostí, samostatností a inteligencí."


class Bird(Animal):
    def make_sound(self):
        return "Vrku!"

    def describe(self):
        return "Pták je dvounohé zvíře s křídly, které má spoustu odlišných a nádherných druhů."

def animal_info(animal):
    messagebox.showinfo("Info zvíře", f"Zvire: {animal.make_sound()}\nPopis: {animal.describe()}")


class ZooApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Zoo Application")

        tk.Label(root, text="Vítejte v Zoo!", font=("Arial", 16)).pack(pady=10)

        self.animals = {
            "Dog": Dog(),
            "Cat": Cat(),
            "Bird": Bird()
        }

        for name, animal in self.animals.items():
            tk.Button(root, text=name, command=lambda a=animal: animal_info(a)).pack(pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = ZooApp(root)
    root.mainloop()
