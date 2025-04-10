import tkinter as tk
from tkinter import messagebox, simpledialog
import os
import json

# ---------- TŘÍDA ZÁZNAM ----------
class Zaznam:
    def __init__(self, nadpis, text):
        self.nadpis = nadpis
        self.text = text

    def to_dict(self):
        return {"nadpis": self.nadpis, "text": self.text}

    @staticmethod
    def from_dict(data):
        return Zaznam(data["nadpis"], data["text"])


# ---------- TŘÍDA DIÁŘ ----------
class Dnar:
    def __init__(self, soubor='diary.txt'):
        self.soubor = soubor
        self.zaznamy = self.nacti()

    def pridej(self, zaznam):
        self.zaznamy.append(zaznam)
        self.uloz()

    def smaz(self, index):
        if 0 <= index < len(self.zaznamy):
            del self.zaznamy[index]
            self.uloz()

    def nacti(self):
        if not os.path.exists(self.soubor):
            return []
        with open(self.soubor, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Zaznam.from_dict(z) for z in data]

    def uloz(self):
        with open(self.soubor, 'w', encoding='utf-8') as f:
            json.dump([z.to_dict() for z in self.zaznamy], f, ensure_ascii=False, indent=2)


# ---------- GUI ----------
class Aplikace:
    def __init__(self, root):
        self.diar = Dnar()

        root.title("Osobní diář")
        root.configure(bg='#e6f2ff')

        font = ("Segoe UI", 10)

        # Vstupy
        self.nadpis_entry = tk.Entry(root, width=40, font=font, bg='white')
        self.nadpis_entry.grid(row=0, column=0, padx=10, pady=5, columnspan=2)

        self.text_entry = tk.Text(root, height=5, width=40, font=font, bg='white')
        self.text_entry.grid(row=1, column=0, padx=10, pady=5, columnspan=2)

        # Tlačítka
        btn_bg = "#cce6ff"
        tk.Button(root, text="Přidat záznam", command=self.pridat, bg=btn_bg, font=font).grid(row=2, column=0, pady=5)
        tk.Button(root, text="Zobrazit záznam", command=self.zobrazit, bg=btn_bg, font=font).grid(row=2, column=1, pady=5)
        tk.Button(root, text="Smazat záznam", command=self.smazat, bg=btn_bg, font=font).grid(row=3, column=0, columnspan=2, pady=5)

        # Seznam záznamů
        self.seznam = tk.Listbox(root, width=50, font=font, bg='white')
        self.seznam.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        self.obnov_seznam()

    def pridat(self):
        nadpis = self.nadpis_entry.get().strip()
        text = self.text_entry.get("1.0", tk.END).strip()
        if not nadpis or not text:
            messagebox.showwarning("Chyba", "Nadpis a text musí být vyplněny.")
            return
        zaznam = Zaznam(nadpis, text)
        self.diar.pridej(zaznam)
        self.nadpis_entry.delete(0, tk.END)
        self.text_entry.delete("1.0", tk.END)
        self.obnov_seznam()

    def zobrazit(self):
        index = self.seznam.curselection()
        if not index:
            messagebox.showinfo("Info", "Vyberte záznam.")
            return
        zaznam = self.diar.zaznamy[index[0]]
        messagebox.showinfo(zaznam.nadpis, zaznam.text)

    def smazat(self):
        index = self.seznam.curselection()
        if not index:
            messagebox.showinfo("Info", "Vyberte záznam ke smazání.")
            return
        potvrzeni = messagebox.askyesno("Potvrzení", "Opravdu chcete záznam smazat?")
        if potvrzeni:
            self.diar.smaz(index[0])
            self.obnov_seznam()

    def obnov_seznam(self):
        self.seznam.delete(0, tk.END)
        for z in self.diar.zaznamy:
            self.seznam.insert(tk.END, z.nadpis)


# ---------- SPUŠTĚNÍ ----------
if __name__ == "__main__":
    root = tk.Tk()
    app = Aplikace(root)
    root.mainloop()