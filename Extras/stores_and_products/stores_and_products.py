class Store:

    def __init__(self, store_name):
        self.store_name = store_name
        self.product_list = []

    def printProduct(self):
        for i in range(len(self.product_list)):
            print(self.product_list[i].product_name)

    def add_product(self, new_product):
        self.product_list.append(new_product)
        # self.printProduct() # Example of how I would associate a Method inside of a Method.

    def sell_product(self, id):
        for l in range(len(self.product_list)):
            # print(self.product_list[l].product_name)
            if l == id:
                self.product_list.pop(id)
                print(f"The product you bought is a {self.product_list[id].product_name}, the category is {self.product_list[id].product_category} and the price for it is ${self.product_list[id].product_price}.")
            else:
                print(self.product_list)

    def inflation(self, percent_increase):
        for j in range(len(self.product_list)):
            self.product_list[j].product_price +=  (self.product_list[j].product_price * percent_increase)
            print(self.product_list[j].product_price)


class Product: # This is my class named Product, it is a Blueprint for what I want to do to an instance object once it is created and set to my class Product (i.e sam = product()).

    def __init__(self, product_name, product_price, product_category): # This is my constructor function or initiator function. This is always my first Method of my class Because this tells the program/interpreter what I want each instance/object thats created and set ,(i.e sam = Product()), to my class Product (i.e sam = Product(self, name, age, height)). Also "SELF" is always the first parameter, Because "SELF" IS THE REPRESENTATION of the instance (i.e sam), So I am basically Passing in the object (sam) into the Methods of my class Using "SELF". The __init__ is called everytime a object is instantiated (i.e brent = Product()).
        self.product_name = product_name # The object/instance being passed into the Attribute using Dot Notation and being SET to the class Product Attribute ,"product_name", for my class. The Instance Attribute (i.e product_name, product_price, product_category) are indicated by "SELF". "SELF" represents the Instance (i.e sam) NOT the class or its Attributes or Methods.
        self.product_price = product_price
        self.product_category = product_category

    def update_price(self, percent_changed, is_increased): # ALL METHODS IN PYTHON HAVE TO HAVE "SELF" AS ITS FIRST ATTRIBUTE/PARAMETER, BECAUSE "SELF" IS THE REPRESENTATION OF THE INSTANCE (i.e sam). Parameters/Attributes are optional with Functions!!! This is a Method that parses and returns (optional/ Also will return None if there is no explicit return statement) a(n) output to the console. And the other two attributes are normal attributes/parameters that take in a String, Integer, List, Dictionary, or any other data type an/or structure. And this Method is for increasing or updating the price of for my instance/object.
        if self.product_price > is_increased:
            self.product_price *= 1 + percent_changed
            self.print_info()
        elif self.product_price < is_increased:
            self.product_price *= 1 - percent_changed
            self.print_info()
        else:
            self.product_price = self.product_price
            self.print_info()

    def print_info(self): # This is a print_info Method to show the user the information about the product.
        print(f"This is the product's information: {self.product_name}, the category is {self.product_category} and the price for it is ${self.product_price}.")


# Created class Product instances
cucumber = Product("Cucumber", 2, "Produce")
tomato = Product("Tomato", 3, "Produce")

# Created class Store Instances
hughes = Store("Reasors")

# Invoking class Product Methods
cucumber.update_price(0.01, 1)
tomato.update_price(0.02, 5)

# Invoking class Store Methods
hughes.add_product(cucumber)
hughes.inflation(0.03)
hughes.add_product(tomato)
# hughes.inflation(0.04)
hughes.sell_product(0)
