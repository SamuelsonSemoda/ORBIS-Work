import tkinter as tk
from tkinter import ttk

class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

stud1 = Student("John", 22, "Computer Science")
stud2 = Student("Jane", 19, "Physics")
stud3 = Student("Samuel", 20, "Astronomy")

students = [stud1, stud2, stud3]

root = tk.Tk()
root.title("Student Information")
root.geometry("500x500")
root.configure(bg="#A7B2FF")

title_label = tk.Label(root, text="Student Details", font=("Arial", 28, "bold"), bg="#A7B2FF")
title_label.pack(pady=10)

tree = ttk.Treeview(root, columns=("Name", "Age", "Major"), show="headings")

tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.heading("Major", text="Major")

tree.column("Name", width=100, anchor=tk.CENTER)
tree.column("Age", width=50, anchor=tk.CENTER)
tree.column("Major", width=120, anchor=tk.CENTER)

tree.pack(pady=10)

for student in students:
    tree.insert("", tk.END, values=(student.name, student.age, student.major))

root.mainloop()
