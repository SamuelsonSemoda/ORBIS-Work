import tkinter as tk
from tkinter import ttk


class StudentTableApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Table")

        window_width = 720
        window_height = 720
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        main_frame = tk.Frame(root)
        main_frame.pack(expand=True)

        self.entries = {}
        fields = ["Name", "School", "Math", "Czech", "Coding"]

        for i, field in enumerate(fields):
            tk.Label(main_frame, text=field, font=("Arial", 12)).grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entry = tk.Entry(main_frame, font=("Arial", 12))
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries[field.lower()] = entry

        tk.Button(main_frame, text="Submit", command=self.add_student, font=("Arial", 12)).grid(row=len(fields),
                                                                                                column=0, columnspan=2,
                                                                                                pady=10)
        columns = fields + ["Average"]
        self.tree = ttk.Treeview(main_frame, columns=columns, show="headings")
        for field in columns:
            self.tree.heading(field, text=field)
            self.tree.column(field, width=75, anchor="center")
        self.tree.grid(row=len(fields) + 1, column=0, columnspan=2, padx=10, pady=5)

    def add_student(self):
        try:
            name = self.entries["name"].get()
            age = self.entries["school"].get()
            math = float(self.entries["math"].get())
            czech = float(self.entries["czech"].get())
            coding = float(self.entries["coding"].get())

            average = round((math + czech + coding) / 3, 2)

            self.tree.insert("", "end", values=(name, age, math, czech, coding, average))

            for entry in self.entries.values():
                entry.delete(0, tk.END)

        except ValueError:
            print("Error: Please enter valid numbers for grades!")


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentTableApp(root)
    root.mainloop()
