import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_age():
    try:
        birthdate = datetime.strptime(entry.get(), "%Y-%m-%d")
        today = datetime.today()

        years = today.year - birthdate.year
        months = today.month - birthdate.month
        days = today.day - birthdate.day

        if days < 0:
            months -= 1
            days += 30  # Approximate month length

        if months < 0:
            years -= 1
            months += 12

        result_label.config(
            text=f"You are {years} years, {months} months, and {days} days old."
        )
    except Exception as e:
        messagebox.showerror("Invalid input", "Please enter date in YYYY-MM-DD format")

# UI Setup
root = tk.Tk()
root.title("Age Calculator")
root.geometry("400x250")
root.config(bg="#f7f7f7")

title = tk.Label(root, text="Age Calculator", font=("Helvetica", 18, "bold"), bg="#f7f7f7")
title.pack(pady=10)

entry_label = tk.Label(root, text="Enter your birthdate (YYYY-MM-DD):", bg="#f7f7f7")
entry_label.pack()

entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=10)

btn = tk.Button(root, text="Calculate Age", command=calculate_age, bg="#4a90e2", fg="white", font=("Arial", 12))
btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14), bg="#f7f7f7", fg="green")
result_label.pack(pady=10)

root.mainloop()
