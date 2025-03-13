import tkinter as tk
from tkinter import messagebox, simpledialog


class Kniha:
    def __init__(self, nazev, autor, rok_vydani):
        self.nazev = nazev
        self.autor = autor
        self.rok_vydani = rok_vydani
        self.dostupna = True

    def vypis_info(self):
        dostupnost = "Ano" if self.dostupna else "Ne"
        return f"Název: {self.nazev}, Autor: {self.autor}, Rok vydání: {self.rok_vydani}, Dostupná: {dostupnost}"

    def vypujcit_knihu(self):
        if self.dostupna:
            self.dostupna = False
            return f"Kniha '{self.nazev}' byla vypůjčena."
        else:
            return f"Kniha '{self.nazev}' není dostupná."

    def vratit_knihu(self):
        if not self.dostupna:
            self.dostupna = True
            return f"Kniha '{self.nazev}' byla vrácena."
        else:
            return f"Kniha '{self.nazev}' je již dostupná."


class Knihovna:
    def __init__(self):
        self.seznam_knih = [
            Kniha("2001: Vesmírná Odysea", "Arthur C. Clarke", 1968),
            Kniha("Osvícení", "Stephen King", 1977),
            Kniha("Hello Neighbor: Missing Pieces", "Carly Anne West", 2018),
            Kniha("Ready Player One", "Ernest Cline", 2011),
            Kniha("1984", "George Orwell", 1949),
            Kniha("Malý princ", "Antoine de Saint-Exupéry", 1943),
            Kniha("Harry Potter a Kámen mudrců", "J.K. Rowling", 1997)
        ]

    def hledat_knihy_podobne(self, nazev):
        podobne_knihy = [kniha for kniha in self.seznam_knih if nazev.lower() in kniha.nazev.lower()]
        return podobne_knihy

def hledat_knihu():
    nazev = entry_hledat.get()
    nalezene_knihy = knihovna.hledat_knihy_podobne(nazev)

    if not nalezene_knihy:
        messagebox.showinfo("Výsledek hledání", "Žádné knihy nebyly nalezeny.")
        return

    knihy_text = "\n".join([f"{i + 1}. {kniha.nazev} ({kniha.autor})" for i, kniha in enumerate(nalezene_knihy)])
    vyber = simpledialog.askinteger("Výběr knihy", f"Nalezené knihy:\n{knihy_text}\nZadejte číslo knihy:", minvalue=1,
                                    maxvalue=len(nalezene_knihy))

    if vyber is not None:
        vybrana_kniha = nalezene_knihy[vyber - 1]
        odpoved = messagebox.askyesno("Vypůjčení knihy", f"{vybrana_kniha.vypis_info()}\nChcete knihu vypůjčit?")
        if odpoved:
            messagebox.showinfo("Vypůjčení", vybrana_kniha.vypujcit_knihu())


def vratit_knihu():
    nazev = entry_hledat.get()
    nalezene_knihy = knihovna.hledat_knihy_podobne(nazev)

    if not nalezene_knihy:
        messagebox.showinfo("Výsledek hledání", "Žádné knihy nebyly nalezeny.")
        return

    knihy_text = "\n".join([f"{i + 1}. {kniha.nazev} ({kniha.autor})" for i, kniha in enumerate(nalezene_knihy)])
    vyber = simpledialog.askinteger("Výběr knihy", f"Nalezené knihy:\n{knihy_text}\nZadejte číslo knihy:", minvalue=1,
                                    maxvalue=len(nalezene_knihy))

    if vyber is not None:
        vybrana_kniha = nalezene_knihy[vyber - 1]
        messagebox.showinfo("Vrácení knihy", vybrana_kniha.vratit_knihu())

knihovna = Knihovna()

root = tk.Tk()
root.title("Správa knihovny")

frame_search = tk.Frame(root)
frame_search.pack()
tk.Label(frame_search, text="Hledat knihu:").pack(side=tk.LEFT)
entry_hledat = tk.Entry(frame_search, width=50)
entry_hledat.pack(side=tk.LEFT)
tk.Button(frame_search, text="Hledat", command=hledat_knihu).pack()
tk.Button(frame_search, text="Vrátit", command=vratit_knihu).pack()

root.mainloop()