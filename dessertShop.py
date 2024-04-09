import tkinter as tk

class DessertShop:
    def __init__(self, master):
        self.master = master
        self.master.title("Dessert Shop")
        
        # frame for radio buttons
        self.left_frame = tk.Frame(self.master)
        self.left_frame.pack(side=tk.LEFT)
        
        # frame for cart textbox
        self.right_frame = tk.Frame(self.master)
        self.right_frame.pack(side=tk.RIGHT)
        
        # dictionary of items with prices
        self.items = {
            "Crossaint": 4.99,
            "Macaron": 9.99,
            "Cream Puff": 6.99,
            "Eclair": 5.99
        }
        
        # item section
        self.var = tk.StringVar(value=None)
        self.radio_buttons = []
        for item, price in self.items.items():
            radio_button = tk.Radiobutton(self.left_frame, text=f"{item}: ${price}", variable=self.var, value=item)
            radio_button.pack(anchor=tk.W)
            self.radio_buttons.append(radio_button)
        
        self.add_to_cart_button = tk.Button(self.left_frame, text="Add to Cart", command=self.add_to_cart)
        self.add_to_cart_button.pack()
        
        # cart textbox section
        self.cart_textbox = tk.Text(self.right_frame, height=10, width=20)
        self.cart_textbox.pack()
        
        # deselect all radio buttons - fixes init selecting all
        self.deselect_all()
    
    # add and output
    def add_to_cart(self):
        selected_item = self.var.get()
        if selected_item:
            self.cart_textbox.insert(tk.END, f"{selected_item}: ${self.items[selected_item]}\n")
    
    def deselect_all(self):
        self.var.set(None)

root = tk.Tk()
launch_app = DessertShop(root)
root.mainloop()
