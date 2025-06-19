import tkinter as tk
from tkinter import messagebox

# ===================== CODER TASK 1: Define Product class =====================
class Product:
    def __init__(self, pid, name, price, quantity):
        self.pid = pid
        self.name = name
        self.price = price
        self.quantity = quantity

# ===================== CODER TASK 2: Define CartItem class ====================
class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

# ===================== CODER TASK 3: Create the main ShoppingCart GUI app ====================
class ShoppingCartApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Online Shopping Cart")

        # ===================== CODER TASK 4: Create product catalog ====================
        self.catalog = {
            "Q1029": Product("Q1029", "Headphones", 50.0, 10),
            "L2374": Product("L2374", "Laptop", 130.0, 20),
            "D2384": Product("D2384", "4K TV", 456.0, 6),
            "W3748": Product("W3748", "Magnetic Powerbank", 78.3, 9),
            "I9374": Product("I9374", "Antivirus", 87.0, 4),
        }

        # ===================== CODER TASK 5: Create cart to hold added items ====================
        self.cart = {}

        # ===================== CODER TASK 6: Display available products ====================
        tk.Label(root, text="Available Products:").pack()
        self.product_listbox = tk.Listbox(root, width=45, bg="#AFC8ED")
        self.product_listbox.pack()
        self.show_products()

        # ===================== CODER TASK 7: Input fields for product ID and quantity ====================
        tk.Label(root, text="Enter Product ID:").pack()
        self.entry_pid = tk.Entry(root, bg="#AFC8ED")
        self.entry_pid.pack()

        tk.Label(root, text="Enter Quantity:").pack()
        self.entry_qty = tk.Entry(root, bg="#AFC8ED")
        self.entry_qty.pack()

        # ===================== CODER TASK 8: Buttons to add items and view total ====================
        tk.Button(root, text="Add to Cart", command=self.add_to_cart).pack(pady=5)
        tk.Button(root, text="View Cart Total", command=self.view_total).pack()
        tk.Button(root, text="Checkout", command=self.checkout).pack(pady=5)  # NEW Checkout button

        # ===================== CODER TASK 9: Display shopping cart ====================
        tk.Label(root, text="Your Cart:").pack()
        self.cart_listbox = tk.Listbox(root, width=45, bg="#AFC8ED")
        self.cart_listbox.pack()

    # ===================== CODER TASK 10: Show all available products ====================
    def show_products(self):
        self.product_listbox.delete(0, tk.END)
        for p in self.catalog.values():
            self.product_listbox.insert(
                tk.END, f"{p.pid} - {p.name} (${p.price}) - Stock: {p.quantity}"
            )

    # ===================== CODER TASK 11: Update cart display with current items ====================
    def update_cart(self):
        self.cart_listbox.delete(0, tk.END)
        for item in self.cart.values():
            subtotal = item.product.price * item.quantity
            self.cart_listbox.insert(
                tk.END,
                f"{item.product.name} x {item.quantity} = ${subtotal:.2f}"
            )

    # ===================== CODER TASK 12: Add product to cart ====================
    def add_to_cart(self):
        pid = self.entry_pid.get().strip()
        try:
            qty = int(self.entry_qty.get())
        except ValueError:
            messagebox.showerror("Input Error", "Quantity must be a number.")
            return

        if qty <= 0:
            messagebox.showerror("Input Error", "Quantity must be positive.")
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
                messagebox.showerror("Stock Error", "Not enough stock available.")
        else:
            messagebox.showerror("Product Error", "Invalid Product ID.")

    # ===================== CODER TASK 13: Calculate and display total amount ====================
    def view_total(self):
        total = sum(item.product.price * item.quantity for item in self.cart.values())
        messagebox.showinfo("Cart Total", f"Total amount: ${total:.2f}")

    # ===================== CODER TASK 14: Checkout and clear cart ====================
    def checkout(self):
        if not self.cart:
            messagebox.showinfo("Checkout", "Your cart is empty!")
            return
        total = sum(item.product.price * item.quantity for item in self.cart.values())
        messagebox.showinfo("Checkout", f"Thank you for your purchase!\nTotal: ${total:.2f}")
        self.cart.clear()
        self.update_cart()

# ===================== CODER TASK 15: Launch the application ====================
if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingCartApp(root)
    root.mainloop()

