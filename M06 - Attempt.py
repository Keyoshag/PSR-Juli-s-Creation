"""""
Program: Juli's Creations Cake Order Request
Author: Keyosha Galvin
Date Written: 07/11/2024
Assignment: Module 06 Project Status
Short Description: This is my first attempt with creating the GUI 
- allowing customer input and display an estimated cost.
"""""

import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Define the main application class


class WeddingCakeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Juli's Creations - Wedding Cake Ordering System")
        self.create_main_window()

    def create_main_window(self):
        tk.Label(self.root, text="Wedding Cake Ordering System").grid(row=0, columnspan=2)

        tk.Label(self.root, text="Wedding Date (MM-DD-YYYY):").grid(row=1, column=0)
        self.date_entry = tk.Entry(self.root)
        self.date_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Number of Guests:").grid(row=2, column=0)
        self.guests_entry = tk.Entry(self.root)
        self.guests_entry.grid(row=2, column=1)

        tk.Label(self.root, text="Desired Number of Tiers:").grid(row=3, column=0)
        self.tiers_entry = tk.Entry(self.root)
        self.tiers_entry.grid(row=3, column=1)

        tk.Label(self.root, text="Color Scheme:").grid(row=4, column=0)
        self.color_entry = tk.Entry(self.root)
        self.color_entry.grid(row=4, column=1)

        tk.Label(self.root, text="Cake Flavor(s):").grid(row=5, column=0)
        self.flavor_entry = tk.Entry(self.root)
        self.flavor_entry.grid(row=5, column=1)

        tk.Label(self.root, text="Desired Frosting Type:").grid(row=6, column=0)
        self.frosting_entry = tk.Entry(self.root)
        self.frosting_entry.grid(row=6, column=1)

        tk.Label(self.root, text="Any Writing:").grid(row=7, column=0)
        self.writing_entry = tk.Entry(self.root)
        self.writing_entry.grid(row=7, column=1)

        tk.Label(self.root, text="Cake Decorations:").grid(row=8, column=0)
        self.decorations_entry = tk.Entry(self.root)
        self.decorations_entry.grid(row=8, column=1)

        tk.Button(self.root, text="Submit", command=self.calculate_cost).grid(row=9, column=0)
        tk.Button(self.root, text="Reset", command=self.reset_entries).grid(row=9, column=1)

    def reset_entries(self):
        self.date_entry.delete(0, tk.END)
        self.guests_entry.delete(0, tk.END)
        self.tiers_entry.delete(0, tk.END)
        self.color_entry.delete(0, tk.END)
        self.flavor_entry.delete(0, tk.END)
        self.frosting_entry.delete(0, tk.END)
        self.writing_entry.delete(0, tk.END)
        self.decorations_entry.delete(0, tk.END)

    def calculate_cost(self):
        # Input validation
        date = self.date_entry.get()
        guests = self.guests_entry.get()
        tiers = self.tiers_entry.get()
        flavor = self.flavor_entry.get()
        customizations = 0

        try:
            datetime.strptime(date, "%m-%d-%Y")
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid date in two digit month/day and four digit year format.")
            return

        try:
            guests = int(guests)
            if guests <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a positive number for the number of guests.")
            return

        try:
            tiers = int(tiers)
            if tiers <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a positive number for the number of tiers.")
            return

        if not flavor:
            messagebox.showerror("Invalid input", "Please enter at least one cake flavor.")
            return

        # Calculating costs
        flavors_count = len(flavor.split(','))
        if flavors_count == 1:
            flavor_cost = 80
        elif flavors_count == 2:
            flavor_cost = 100
        else:
            flavor_cost = 150

        if self.color_entry.get():
            customizations += 1
        if self.frosting_entry.get():
            customizations += 1
        if self.writing_entry.get():
            customizations += 1
        if self.decorations_entry.get():
            customizations += 1

        customization_cost = customizations * 30
        tiers_cost = tiers * 25
        total_cost = flavor_cost + customization_cost + tiers_cost

        self.show_confirmation(date, guests, tiers, flavor, total_cost)

    def show_confirmation(self, date, guests, tiers, flavor, total_cost):
        confirmation_window = tk.Toplevel(self.root)
        confirmation_window.title("Order Confirmation")

        tk.Label(confirmation_window, text="Order Confirmation").grid(row=0, columnspan=2)

        tk.Label(confirmation_window, text="Wedding Date:").grid(row=1, column=0)
        tk.Label(confirmation_window, text=date).grid(row=1, column=1)

        tk.Label(confirmation_window, text="Number of Guests:").grid(row=2, column=0)
        tk.Label(confirmation_window, text=guests).grid(row=2, column=1)

        tk.Label(confirmation_window, text="Desired Number of Tiers:").grid(row=3, column=0)
        tk.Label(confirmation_window, text=tiers).grid(row=3, column=1)

        tk.Label(confirmation_window, text="Cake Flavor(s):").grid(row=4, column=0)
        tk.Label(confirmation_window, text=flavor).grid(row=4, column=1)

        tk.Label(confirmation_window, text="Estimated Cost:").grid(row=5, column=0)
        tk.Label(confirmation_window, text=f"${total_cost}").grid(row=5, column=1)

        tk.Label(confirmation_window, text="Final costing will be confirmed directly through the bakery.").grid(row=6, columnspan=2)

        tk.Button(confirmation_window, text="Close", command=confirmation_window.destroy).grid(row=7, columnspan=2)


if __name__ == "__main__":
    root = tk.Tk()
    app = WeddingCakeApp(root)
    root.mainloop()
