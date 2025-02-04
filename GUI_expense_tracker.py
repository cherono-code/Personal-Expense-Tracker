import sys
import tkinter as tk
from tkinter import ttk, messagebox
from expense_manager import setup_db, add_expense, load_expenses

setup_db()  # Ensure the database is ready

# Function to add expense via GUI
def add_expense_gui():
    amount = amount_entry.get()
    category = category_var.get()
    description = description_entry.get()
    date = date_entry.get()

    if not amount or not category or not date:
        messagebox.showerror("Error", "Please fill all required fields!")
        return
    
    try:
        add_expense(float(amount), category, description, date)
        amount_entry.delete(0, tk.END)
        description_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)
        category_var.set(categories[0])
        load_expenses_gui()
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number!")

# Function to load expenses into the table
def load_expenses_gui():
    for row in table.get_children():
        table.delete(row)
    
    for row in load_expenses():
        table.insert("", tk.END, values=row)

# GUI Setup
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("500x400")

# Input Fields
tk.Label(root, text="Amount:").grid(row=0, column=0, padx=10, pady=5)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1, padx=10, pady=5)

categories = ["Food", "Transport", "Shopping", "Bills", "Other"]
category_var = tk.StringVar(value=categories[0])
tk.Label(root, text="Category:").grid(row=1, column=0, padx=10, pady=5)
category_dropdown = ttk.Combobox(root, textvariable=category_var, values=categories)
category_dropdown.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Description:").grid(row=2, column=0, padx=10, pady=5)
description_entry = tk.Entry(root)
description_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Date (YYYY-MM-DD):").grid(row=3, column=0, padx=10, pady=5)
date_entry = tk.Entry(root)
date_entry.grid(row=3, column=1, padx=10, pady=5)

# Buttons
tk.Button(root, text="Add Expense", command=add_expense_gui).grid(row=4, column=0, columnspan=2, pady=10)

# Expense Table
columns = ("Amount", "Category", "Description", "Date")
table = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    table.heading(col, text=col)
    table.column(col, width=100)
table.grid(row=5, column=0, columnspan=2, pady=10)

load_expenses_gui()

root.mainloop()
