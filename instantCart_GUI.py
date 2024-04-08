from tkinter import *
from instantCart_CLASS import Item
from instantCart_CLASS import SmartCart
from functools import partial
import random, string 

class MyFrame(Frame):
    def __init__(self, root):
        '''Constructor method'''
        Frame.__init__(self, root) # Frame class initialization
        self.init_container() # initialize all widget containers
        self.cart = SmartCart() # initialize SmartCart dict object - key = Item object item selected, value = quantity
        self.welcome() 
        self.data = StringVar(self, 'Subtotal: 0.0') #Associated with subtotal label
        
    def init_container(self):
        '''Initialize widget containers'''
        self.quantity_entries = [] # quantity entry list
        self.states = [] # holds state if selected/not i-th list item holds selection for i-th item
 
    def clear_frame(self): 
        '''Clears the previous frame'''
        for widget in self.winfo_children():
            widget.destroy()

    def exit_application(self):
        '''Exits the program'''
        root.destroy()

    def welcome(self):
        '''1. Welcome window'''
        self.clear_frame()
        Label(self, text = '****Welcome to Instant Cart!****', background="gray70").pack(side = TOP)
        #your code here
        #Start Ordering: Button – start the program, command = shop_by_category
        Button(self, text = "Start Ordering", command = self.shop_by_category).pack()
        #Exit Application: Button – exit the program, command = exit_application
        Button(self, text = "Exit Application", command = self.exit_application).pack()
        

    def shop_by_category(self):
        '''2. Widget to display different category of items'''
        self.clear_frame()
        self.init_container()
        #your code here
        #a.	Choose Category: label
        Label(self, text = 'Choose Category', background="gray70").pack(side = TOP)
        #b.	Dairy: Button – command = start (code below)
        #partial is a special method to pass an argument during button command
        #for dairy category Item.dairy_items will be passed to display all dairy item
        self.dairy_button  = Button(self, text = "Dairy", command = partial(self.start, Item.dairy_items)).pack()
        #your code here
        #c.	Vegetable and Fruit - veg_fruit_button: Button – command = start (Same as dairy)
        self.veg_fruit_button  = Button(self, text = "Vegetable and Fruit", command = partial(self.start, Item.veg_fruit_items)).pack()
        #d.	Poultry and Meat - poultry_meat_button: Button – command = start(Same as dairy)
        self.poultry_meat_button  = Button(self, text = "Poultry and Meat", command = partial(self.start, Item.meat_items)).pack()
        #e.	Seafood: Button - seafood_button – command = start(Same as dairy)
        self.seafood_button  = Button(self, text = "Seafood", command = partial(self.start, Item.seafood_items)).pack()
        #f.	Go Back: Button – command = welcome (go back to #1)
        self.back_button  = Button(self, text = "Go Back", command = self.welcome).pack()
        
        #layout manager for all the widgets
##        self.dairy_button.grid(row = 0)
##        self.veg_fruit_button(row = 1)
##        self.poultry_meat_button(row = 2)
##        self.back_button(row = 3)
        
    def start(self, current_items):
        ''''3. Start ordering from selected category,
        list passed by command will be used as current_items'''
        self.clear_frame()
        self.init_container()


        row = 0
        
        l1 = Label(self, text = 'Select item(s) and enter quantity', background="gray70")
        l1.grid(row = row, column = 1)
        #creating widgets for items using a for loop
        #iterative over each item of current items and
        #create that many checkbutton, price and unit label,and quantity entry
        
        for item in current_items:
            self.states.append(IntVar()) #keeps track if an item is selected
            checkbutton = Checkbutton(self, text=item.get_name(), variable=self.states[row]) #create check buttons
            checkbutton.grid(row = row, column = 0)

            #your code here
            #create and layout a price label, set text to item.get_price()
            price_label = Label(self, text = '$' + str(item.get_price()))
            price_label.grid(row = row, column = 1)
            #create and layout a quantity entry and append to quantity_entries, set width = 2
            e = Entry(self, width = 2)
            e.grid(row = row, column = 2)
            self.quantity_entries.append(e)
            #create and layout unit_label and set text to item.get_unit() function            
            unit_label = Label(self, text = item.get_unit())
            unit_label.grid(row = row, column = 3)
            
            row+=1
        #create and layout subtotal lable, set textvaribale = self.data so it changes
        #with each add_to_cart button being pressedng
        self.total_label = Label(self, textvariable = self.data)
        self.total_label.grid(column = 0)
        #create and layout select categories: button, command = shop_by_category
        self.checkout_button = Button(self, text = 'Select Categories', command = self.shop_by_category)
        self.checkout_button.grid(column = 3)
        #create and layout add_to_cart_button, command = partial(self.add_to_cart, current_items)
        self.add_to_cart_button = Button(self, text = 'Add to Cart', command = partial(self.add_to_cart, current_items))
        self.add_to_cart_button.grid(column = 3)
        #create and layout button: checkout, command = self.checkout
        self.checkout_button = Button(self, text = 'Checkout', command = self.checkout)
        self.checkout_button.grid(column = 3)

    def add_to_cart(self, current_items):         
        '''3. Added to cart, displays subtotal'''

        current_subtotal = 0
        for i in range(len(current_items)):
            #your code here
            #get() the value of i-th item of self.states -> returns 1 if selected otherwise 0
            product_name = current_items[i].get_name()
            if (self.states[i].get() == 1): # check if item selected
                #get the product quantity from quantity_entries using get() function
                product_quantity = float(self.quantity_entries[i].get())
                #add item to self.cart dict where k = item object, v = quantity
                product_price = float(current_items[i].get_price())
                current_subtotal += product_quantity * product_price
##                for k,v in self.cart.items():
##                    self.cart.items[product_name] = product_quantity
                    
        #your code here
        #set the StringVar to be the current subtotal (SmartCart object self.cart has subtotal method)
        #refer to class file
        subtotal = self.data.set('Subtotal: {:.2f}'.format(current_subtotal))
        subtotal.grid(row = 5)
        
    def get_receipt_number(self):
        '''Generate random receipt number'''
        return  ''.join(random.choices(string.ascii_letters.upper() + string.digits, k=4))

    def checkout(self):
        '''4. Check out window '''
        self.clear_frame()
        #your code here to create and layout following widgets:
        #refer to receipt frame
        #    Your e-receipt: Label
        Label(self, text = 'Your e-Receipt', background="gray70").pack(side = TOP)
        #    Receipt Number: Label - Randomly generated by program - text = get_receipt_number()
        Label(self, text = self.get_receipt_number()).pack()
        #	Name Price Quantity Unit: Header Label
        Label(self, text = 'name     price     quantity     unit').pack()

        #	Item purchased, price quantity, unit: Label - from cart dictionary using self.cart.items()
        for k, v in self.cart.items():
            Label(self, text = k.get_name() + k.get_price() + v.get_quantity() + v.get_unit()).pack()
        #	Subtotal: Label - get self.cart subtotal - new label 
        #	Tax: Label - 4.3%
        Label(self, text = 'Subtotal: {:.2f}'.format(self.cart.subtotal())).pack()
        #	Total: Label - subtotal + tax
        final_subtotal = float(self.cart.subtotal())
        final_total = final_subtotal + 4.3
        
        Label(self, text = 'Tax: 4.30').pack()
        Label(self, text = 'Total: ').pack()
        #	‘Thank you’ message: Label
        Label(self, text = 'Thank you for using Instant Cart!').pack()
        Label(self, text = '*********************').pack()
        #	Exit application: Button – exit the program- command = exit_application
        Button(self, text = "Exit Application", command = self.exit_application).pack()

#main driver code
root = Tk()
root.title("Instant Cart")
frame = MyFrame(root)
frame.grid()
root.mainloop()
