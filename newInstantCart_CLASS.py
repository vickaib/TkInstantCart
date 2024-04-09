class Item(object):
    '''Item class defines an item
    available in store. Item object saved in
    lists per category'''
    dairy_items = [] 
    produce_items = [] 
    meat_items = [] 
    seafood_items = [] 
    
    def __init__(self, category, name, price, unit):
        '''Initialization method'''
        self.__category = category.lower()
        self.__name = name
        self.__price = price
        self.__unit = unit
        
        # append to list as per category
        if self.__category == 'Dairy'.lower():
            Item.dairy_items.append(self)
            
        elif self.__category == 'Vegetable'.lower():
            Item.produce_items.append(self)

        elif self.__category == 'Fruit'.lower():
            Item.produce_items.append(self)

        elif self.__category == 'Poultry'.lower():
            Item.meat_items.append(self)

        elif self.__category == 'Meat'.lower():
            Item.meat_items.append(self)

        elif self.__category == 'Seafood'.lower():
            Item.seafood_items.append(self)
            
    def get_category(self):
        '''Return category of an item'''
        return self.__category

    def get_name(self):
        '''Return name of an item'''
        return self.__name

    def get_price(self):
        '''Return price of an item'''
        return self.__price
    
    def get_unit(self):
        '''Return unit of an item'''
        return self.__unit

    def __str__(self):
        line = '{}, {}, {}, {}'.format(self.get_category(), self.get_name(), \
                                        self.get_price(), self.get_unit())
        return line

# process file
with open('grocery_list.txt') as l:
    for line in l:
        name, category, price, unit = line.split('|') # split information
        Item(category, name, price, unit) # create Item object
        



