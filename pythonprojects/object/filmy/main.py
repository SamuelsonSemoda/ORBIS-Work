import os
import tkinter as tk
from tkinter import messagebox, simpledialog


class Film:
    def __init__(self, nazev, reziser, rok_vydani, zanr):
        self.nazev = nazev
        self.reziser = reziser
        self.rok_vydani = rok_vydani
        self.zanr = zanr

    def __str__(self):
        return f"{self.nazev} | {self.reziser} | {self.rok_vydani} | {self.zanr}"

    @staticmethod
    def from_string(data):
        nazev, reziser, rok_vydani, zanr = data.strip().split(" | ")
        return Film(nazev, reziser, int(rok_vydani), zanr)


class FilmovaKolekce:
    def __init__(self):
        self.filmy = []

    def pridat_film(self, film):
        self.filmy.append(film)
        messagebox.showinfo("Přidání filmu", f"Film '{film.nazev}' byl přidán do kolekce.")

    def vypsat_filmy(self):
        if not self.filmy:
            messagebox.showinfo("Seznam filmů", "Kolekce je prázdná.")
            return
        filmy_text = "\n".join([str(film) for film in self.filmy])
        messagebox.showinfo("Seznam filmů", filmy_text)

    def ulozit_do_souboru(self, soubor):
        with open(soubor, "w", encoding="utf-8") as f:
            for film in self.filmy:
                f.write(str(film) + "\n")
        messagebox.showinfo("Uložení", f"Filmy byly uloženy do souboru {soubor}.")

    def nacist_ze_souboru(self, soubor):
        if not os.path.exists(soubor):
            messagebox.showwarning("Načítání", "Soubor neexistuje, začínáme s prázdnou kolekcí.")
            return
        with open(soubor, "r", encoding="utf-8") as f:
            self.filmy = [Film.from_string(line) for line in f if line.strip()]
        messagebox.showinfo("Načítání", f"Filmy byly načteny ze souboru {soubor}.")


# GUI aplikace
kolekce = FilmovaKolekce()
kolekce.nacist_ze_souboru("filmy.txt")


def pridat_film_gui():
    nazev = simpledialog.askstring("Přidání filmu", "Zadejte název filmu:")
    reziser = simpledialog.askstring("Přidání filmu", "Zadejte režiséra filmu:")
    rok_vydani = simpledialog.askinteger("Přidání filmu", "Zadejte rok vydání:")
    zanr = simpledialog.askstring("Přidání filmu", "Zadejte žánr filmu:")
    if nazev and reziser and rok_vydani and zanr:
        kolekce.pridat_film(Film(nazev, reziser, rok_vydani, zanr))


def zobraz_filmy_gui():
    kolekce.vypsat_filmy()


def ulozit_filmy_gui():
    kolekce.ulozit_do_souboru("filmy.txt")


root = tk.Tk()
root.title("Správa filmové kolekce")

frame = tk.Frame(root)
frame.pack(pady=20)

tk.Button(frame, text="Přidat film", command=pridat_film_gui).pack(pady=5)
tk.Button(frame, text="Zobrazit filmy", command=zobraz_filmy_gui).pack(pady=5)
tk.Button(frame, text="Uložit filmy", command=ulozit_filmy_gui).pack(pady=5)

root.mainloop()