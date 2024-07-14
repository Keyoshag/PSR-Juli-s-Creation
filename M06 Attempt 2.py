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


class WeddingCakeOrderApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Wedding Cake Ordering System for Juli’s Creations")
        self.geometry("500x500")

        # Labels
        self.create_label("Wedding Date (MM/DD/YYYY):", 0)
        self.create_label("Number of Guests:", 1)
        self.create_label("Number of Tiers:", 2)
        self.create_label("Color Scheme:", 3)
        self.create_label("Cake Flavor:", 4)
        self.create_label("Frosting Type:", 5)
        self.create_label("Writing on Cake:", 6)
        self.create_label("Cake Decorations:", 7)

        # Entry fields
        self.date_entry = self.create_entry(0)
        self.guests_entry = self.create_entry(1)
        self.tiers_entry = self.create_entry(2)
        self.color_entry = self.create_entry(3)
        self.flavor_entry = self.create_entry(4)
        self.frosting_entry = self.create_entry(5)
        self.writing_entry = self.create_entry(6)
        self.decorations_entry = self.create_entry(7)

        # Submit button
        self.submit_button = tk.Button(self, text="Submit Order", command=self.calculate_cost)
        self.submit_button.grid(row=8, column=1)

    def create_label(self, text, row):
        label = tk.Label(self, text=text)
        label.grid(row=row, column=0, padx=10, pady=5, sticky=tk.W)

    def create_entry(self, row):
        entry = tk.Entry(self)
        entry.grid(row=row, column=1, padx=10, pady=5)
        return entry

    def calculate_cost(self):
        try:
            guests = int(self.guests_entry.get())
            tiers = int(self.tiers_entry.get())
            flavor_count = len(self.flavor_entry.get().split(","))
            customizations = len(self.decorations_entry.get().split(",")) + int(bool(self.writing_entry.get()))

            base_cost = 0
            if flavor_count == 1:
                base_cost = 80
            elif flavor_count == 2:
                base_cost = 100
            else:
                base_cost = 150

            total_cost = base_cost + (tiers * 25) + (customizations * 30)

            message = f"Estimated Cost: ${total_cost}\n"
            message += "Final costing will be confirmed directly through the bakery."

            messagebox.showinfo("Order Summary", message)

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for guests and tiers.")


if __name__ == "__main__":
    app = WeddingCakeOrderApp()
    app.mainloop()
