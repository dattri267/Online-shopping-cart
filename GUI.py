
import tkinter as tk
from tkinter import messagebox

# Product class
class Product:
    def __init__(self, pid, name, price, quantity):
        self.pid = pid
        self.name = name
        self.price = price
        self.quantity = quantity

# Cart item class
class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

class ShoppingCartApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Online Shopping Cart")

        # Sample products
        self.catalog = { 
            "Q1029": Product("Q1029", "Headphones", 50.0, 10),
            "L2374": Product("L2374", "Laptop", 130.0, 20),
            "D2384": Product("D2384","4k TV's",456.0,6),
            "W3748": Product("W3748","Magnetic powerbank",78.30,9),
            "I9374": Product("I9374","Antivirus",87.0,4)
        }

        self.cart = {}

        # Product list
        tk.Label(root, text="Products:").pack()
        self.product_listbox = tk.Listbox(root,bg="#AFC8ED", width=40)
        self.product_listbox.pack()
        self.show_products()

        # Input fields
        tk.Label(root, text="Enter Product ID:").pack()
        self.entry_pid = tk.Entry(root,bg="#AFC8ED")
        self.entry_pid.pack()

        tk.Label(root, text="Enter Quantity:").pack()
        self.entry_qty = tk.Entry(root,bg="#AFC8ED")
        self.entry_qty.pack()

        # Buttons
        tk.Button(root, text="Add to Cart", command=self.add_to_cart).pack(pady=5)
        tk.Button(root, text="View Cart Total", command=self.view_total).pack()

        # Cart display
        tk.Label(root, text="Cart:").pack()
        self.cart_listbox = tk.Listbox(root,bg="#AFC8ED", width=40)
        self.cart_listbox.pack()

    def show_products(self):
        self.product_listbox.delete(0, tk.END)
        for p in self.catalog.values():
            self.product_listbox.insert(tk.END, f"{p.pid} - {p.name} (${p.price}) - Qty: {p.quantity}")

    def update_cart(self):
        self.cart_listbox.delete(0, tk.END)
        for item in self.cart.values():
            name = item.product.name
            qty = item.quantity
            subtotal = item.product.price * qty
            self.cart_listbox.insert(tk.END, f"{name} x {qty} = ${subtotal:.2f}")

    def add_to_cart(self):
        pid = self.entry_pid.get().strip()
        try:
            qty = int(self.entry_qty.get())
        except ValueError:
            messagebox.showerror("Error", "Quantity must be a number.")
            return

        if qty <= 0:
            messagebox.showerror("Error", "Quantity must be positive.")
            return

        if pid in self.catalog:
            product = self.catalog[pid]
            if product.quantity >= qty:
                product.quantity -= qty
                if pid in self.cart:
                    self.cart[pid].quantity += qty
                else:
                    self.cart[pid] = CartItem(product, qty)
                self.show_products()
                self.update_cart()
                self.entry_pid.delete(0, tk.END)
                self.entry_qty.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Not enough stock.")
        else:
            messagebox.showerror("Error", "Invalid Product ID.")

    def view_total(self):
        total = sum(item.product.price * item.quantity for item in self.cart.values())
        messagebox.showinfo("Total", f"Cart total: ${total:.2f}")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingCartApp(root)
    root.mainloop()
    Sample products
   