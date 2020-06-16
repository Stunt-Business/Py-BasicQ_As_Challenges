# ---------------------------------------------------
# Author    :  Benjamin Kataliko Viranga
# Community :  Stunt Business
# Community website : www.stuntbusiness.com
#
# 30 Days - Q&A Python Basic
# Day 26 : 16-06-2020
# Day 26 | IG : https://www.instagram.com/benjivrik/
# Subject : Challenge XIII Create a class Product using OOP
#----------------------------------------------------
# what would be the output of this program ?
'''

    Well, this class is mainly related to a Product 
    you can find in a store.

    Assign a name, a price and an inventory to your Product.

    This should be really basic. 

    Let the user be allowed to changed the product name, price
    and inventory whenever he wants.

    Assign 3 Products to a dictionary where the key is the 
    Product name and the price is the value of the key.

    dictionary[key] = value.

'''

class Product:

    # initialization of your product
    def __init__(self, name, price, inventory):
        '''
            str - name
            float - price
            float - inventory
        '''
        self.__name = name  # product name
        self.__price = price # product price
        self.__inventory = inventory # product inventory (number of items)
    
    # get the name of the product
    def get_name(self):
        return self.__name
    
    # change the name of the product
    def set_name(self, name):
        self.__name = name
        print("New product name set successfully for '{}'.\n".format(self.__name))
    
    # get price of the product
    def get_price(self):
        return self.__price
    
    # change the price of the product
    def set_price(self,price):
        self.__price = price
        print("New price set successfully for '{}'.\n".format(self.__name))
    
    # get the number of items in the inventory of the product
    def get_inventory(self):
        return self.__inventory
    
    # set the inventory value
    def set_inventory(self, inventory):
        self.__inventory = inventory
        print("The inventory of the product '{}' has been updated.".format(self.__name))

    # string representation of your object
    def __str__(self):
        product = "\nYour product '{}' has {} items available in the inventory.\n".format(self.__name, str(self.__inventory))
        product = product + "The current price of your product is ${}.\n".format(self.__price)
        return product

if __name__ == "__main__":
    # creating 3 products
    pineapple =  Product('pineapple', 15,2)
    banana =  Product('banana', 30,8)
    apple =  Product('Apple', 35,6)

    print(pineapple)
    print(banana)
    print(apple)

    # changing the price of pineapple
    pineapple.set_price(40)
    print(pineapple)

    # initializing the dictionary
    items = {}
    items[pineapple.get_name()] = pineapple.get_price()
    items[banana.get_name()] =  banana.get_price()
    items[apple.get_name()] = apple.get_price()

    # priting your dictionary
    print(items)