import tkinter as tk
from tkinter import ttk
from newInstantCart_CLASS import Item

class WelcomeWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Instant Cart")
        self.master.configure(bg="#f0f0f0")  # background color of app
        
        self.welcome_label = tk.Label(self.master, text="Welcome to Instant Cart!", 
                                      font=("Helvetica", 24, "bold"), 
                                      bg="#f0f0f0", 
                                      fg="#333333")  
        self.welcome_label.pack(pady=(50,20))  # add vertical padding

        self.button_frame = tk.Frame(self.master, bg="#f0f0f0")  # container for buttons
        self.button_frame.pack()

        self.start_button = tk.Button(self.button_frame, text="Start Ordering", command=self.start_ordering, 
                                      font=("Helvetica", 14, "bold"), 
                                      bg="#007bff", 
                                      fg="white", 
                                      padx=20, 
                                      pady=10, 
                                      borderwidth=0)  # set font, colors, padding, and remove border
        self.start_button.pack(side=tk.LEFT, pady=0, padx=10)

        self.exit_button = tk.Button(self.button_frame, text="Exit", command=self.exit_app, 
                                     font=("Helvetica", 14, "bold"), 
                                     bg="#dc3545", 
                                     fg="white", 
                                     padx=20, 
                                     pady=10, 
                                     borderwidth=0) 
        self.exit_button.pack(side=tk.LEFT, pady=10, padx=10)

    def start_ordering(self):
        self.master.destroy()  # close welcome menu
        root = tk.Tk()  # begin ordering app
        #root.geometry("500x300")
        launch_app = InstantCart(root)
        root.mainloop()
        
    def exit_app(self):
        self.master.destroy() 

class InstantCart:
    def __init__(self, master):
        self.master = master
        self.master.title("Instant Cart")

        # experimental list for adding values
        self.items = {
            "Apples": 2.50,
            "Bananas": 1.50,
            "Oranges": 3.00,
            "Milk": 3.50,
            "Bread": 2.00
        }

        self.departments = [
            "Dairy",
            "Produce",
            "Meat",
            "Seafood"
        ]

        self.selected_items = {}
        self.total_price = tk.DoubleVar()

        self.create_header()
        self.create_widgets()
    
    def create_header(self):
        self.header = tk.Frame(self.master, bg="#007bff", padx=10, pady=10)
        self.header.grid(row=0, column=0, columnspan=10, sticky="ew")

        self.back_button = tk.Button(self.header, text="< Back to Main Menu", command=self.back_to_menu, 
                                     font=("Helvetica", 10), 
                                     bg="#007bff",
                                     fg="white", 
                                     padx=0, 
                                     pady=0, 
                                     borderwidth=0,
                                     anchor="w") 
        self.back_button.pack(side=tk.LEFT)

    def create_widgets(self):                      
        self.item_label = tk.Label(self.master, text="Select Department:")
        self.item_label.grid(row=1, column=0, padx=5, pady=0, sticky="w")
        
        # combobox dropdown with ttk
        self.dept_select = ttk.Combobox(self.master, values=[*self.departments])
        self.dept_select.grid(row=1, column=1, padx=5, pady=10)
        self.dept_select.bind("<<ComboboxSelected>>", self.on_select)

        # item quantity entry
        self.quantity_label = tk.Label(self.master, text="Quantity:")
        self.quantity_label.grid(row=1, column=2, padx=5, sticky="w")
        self.quantity_entry = tk.Entry(self.master)
        self.quantity_entry.grid(row=1, column=3, padx=5, sticky="w")
        self.add_button = tk.Button(self.master, text="Add", command=self.add_to_list)
        self.add_button.grid(row=1, column=4, padx=5, pady=10)
        
        # list output area
        self.cart_text = tk.Text(self.master, height=5)
        self.cart_text.grid(row=2, column=0, columnspan=5, padx=5, sticky="we")
        
        # total price of items added
        self.total_label = tk.Label(self.master, text="Subtotal:")
        self.total_label.grid(row=11, column=2, padx=10, pady=0)
        self.total_display = tk.Label(self.master, textvariable=self.total_price)
        self.total_display.grid(row=11, column=3)

        self.add_button = tk.Button(self.master, text="Continue to Checkout >")
        self.add_button.grid(row=8, column=2, columnspan=2, padx=10, pady=0)

    # listens for department change and displays respective grocery items 
    def on_select(self, event):
        selected_dept = self.dept_select.get()
        self.dept_products = []

        if selected_dept == "Dairy":
            self.dept_products = Item.dairy_items
        elif selected_dept == "Produce":
            self.dept_products = Item.produce_items
        elif selected_dept == "Meat":
            self.dept_products = Item.meat_items
        elif selected_dept == "Seafood":
            self.dept_products = Item.seafood_items

        # output items
        row = 3
        for product in self.dept_products:
            name_label = tk.Label(self.master, text = str(product.get_name()))
            name_label.grid(row = row, column = 0, sticky="w", padx=10)
            price_label = tk.Label(self.master, text = '$' + str(product.get_price()))
            price_label.grid(row = row, column = 1)
            row += 1

    def add_to_list(self):
        item = self.item_var.get()
        quantity = self.quantity_entry.get()
        
        try:
            quantity = int(quantity)
            if quantity <= 0:
                raise ValueError
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter a valid quantity.")
            return
        
        if item in self.selected_items:
            self.selected_items[item] += quantity
        else:
            self.selected_items[item] = quantity
        
        self.update_cart()

    def update_cart(self):
        self.cart_text.delete(1.0, tk.END)
        total_price = 0
        for item, quantity in self.selected_items.items():
            price = self.items[item]
            total_price += price * quantity
            self.cart_text.insert(tk.END, f"{item}: {quantity} x ${price:.2f}\n")
        
        self.total_price.set(f"${total_price:.2f}")

    def back_to_menu(self):
        self.master.destroy()
        root = tk.Tk()  # recreate the welcome window
        root.geometry("500x300")
        launch_app = WelcomeWindow(root)
        root.mainloop()

root = tk.Tk()  # root instance
frame = WelcomeWindow(root)
root.geometry("500x300")
root.mainloop()


