############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Import settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lab3django.settings')

# setup django environment
import django
django.setup()

# Import your models for use in your script
from mainapp.models import *

############################################################################
## START OF APPLICATION
############################################################################
""" Replace the code below with your own """
# Clear any existing data to avoid duplicate entries
Product.objects.all().delete()

# Insert sample products into the database
Product.objects.create(upc="1234", name="Red Apple", price=0.99)
Product.objects.create(upc="5678", name="Banana", price=0.79)
Product.objects.create(upc="4321", name="Orange Juice", price=3.49)
Product.objects.create(upc="8765", name="Milk", price=2.29)
Product.objects.create(upc="1937", name="Loaf of Bread", price=2.99)

# Print confirmation and product list
print("Product database populated successfully!\n")
for p in Product.objects.all():
    print(f"UPC: {p.upc}\tName: {p.name}\tPrice: ${p.price}")

    
import random
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox

class RegisterView:
    def __init__(self, root):
        root.title("Cash Register")
        root.geometry("450x350")

        frame_center = ttk.Frame(root)
        frame_center.pack(expand=True, fill="both", padx=10, pady=10)

        self.item_list = tk.Text(frame_center, state="disabled", wrap="none", height=12)
        self.item_list.pack(side="left", expand=True, fill="both")

        scrollbar = ttk.Scrollbar(frame_center, orient="vertical", command=self.item_list.yview)
        self.item_list.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        bottom = ttk.Frame(root)
        bottom.pack(fill="x", padx=10, pady=6)

        self.scan_button = ttk.Button(bottom, text="Scan Item")
        self.scan_button.pack(side="left")

        self.random_scan_button = ttk.Button(bottom, text="Random Scan")
        self.random_scan_button.pack(side="left", padx=8)

        self.subtotal_label = ttk.Label(bottom, text="Subtotal: $0.00")
        self.subtotal_label.pack(side="right")

    def update_item_list(self, items):
        self.item_list.config(state="normal")
        self.item_list.delete("1.0", tk.END)
        for upc, name, price in items:
            self.item_list.insert(tk.END, f"{name} - ${price:.2f}\n")
        self.item_list.config(state="disabled")

    def update_subtotal(self, subtotal):
        self.subtotal_label.config(text=f"Subtotal: ${subtotal:.2f}")

class RegisterController:
    def __init__(self, view):
        self.view = view
        self.items = []

        view.scan_button.config(command=self.scan_item)
        view.random_scan_button.config(command=self.random_scan)

        self.all_products = list(Product.objects.all())

    def scan_item(self):
        upc = simpledialog.askstring("Scan UPC", "Enter UPC code:")
        if not upc:
            return
        try:
            prod = Product.objects.get(upc=upc)
            price = float(prod.price)
            self.items.append((prod.upc, prod.name, price))
            self.view.update_item_list(self.items)
            self.view.update_subtotal(sum(i[2] for i in self.items))
        except Product.DoesNotExist:
            messagebox.showerror("Not found", f"No product with UPC {upc} found.")

    def random_scan(self):
        if not self.all_products:
            messagebox.showwarning("No products", "No products available in the database.")
            return
        prod = random.choice(self.all_products)
        price = float(prod.price)
        self.items.append((prod.upc, prod.name, price))
        self.view.update_item_list(self.items)
        self.view.update_subtotal(sum(i[2] for i in self.items))
        messagebox.showinfo("Random Scan",
                            f"UPC: {prod.upc}\nProduct: {prod.name}\nPrice: ${prod.price:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    view = RegisterView(root)
    controller = RegisterController(view)
    root.mainloop()
