# Defining Class (PascalCased)
class Store:

    def __init__(self, store_name):
        self.store_name = store_name
        # Default Value for Product List
        self.product_list = []

# Prints the name of each Product in the List of Products
    def print_product(self):
        for i in range(len(self.product_list)):
            print(self.product_list[i].product_name)
        return self

# Adds Products to the List of Products
    def add_product(self, new_product):
        self.product_list.append(new_product)
# Example of how I would associate a Method inside of a Method.
        self.print_product()
        return self

# Method to "sell" or Remove a Product from the List
    def sell_product(self, id):
        for item in range(len(self.product_list)):
            # Using Print Statements
            # print(self.product_list[item].product_name)
            if item == id:
                print(f"The product you bought was a {self.product_list[id].product_name}, Category - {self.product_list[id].product_category}, the Price for it was ${self.product_list[id].product_price}.")
                self.product_list.pop(id)
        return self

# Method to add Inflation to each of the Product's Price in the List of Products
    def inflation(self, percent_increase):
        for an_item in range(len(self.product_list)):
            self.product_list[an_item].product_price += (self.product_list[an_item].product_price * percent_increase)
            print(self.product_list[an_item].product_price)
        return self


"""
Defining Class named Product,
it is a Blueprint for what I want to do to and what my instance object will have once it is created
"""
class Product:

# This is my constructor function or initiator function. This is always my First Method of my class Because this tells the program/interpreter what I want each instance/object thats created and Instantiated ,(i.e sam = Product()), to my Class Product. Also "SELF" is always the first parameter, Because "SELF" is the REPRESENTATION of the instance (i.e Product), So I am basically Passing in the reference of the object itself into the Methods of my Blueprint by using "SELF". The __init__ is called anytime a object is instantiated (i.e sammy = Product()).
    def __init__(self, product_name, product_price, product_category):
# Assigning Attribute's using Dot Notation that will be attached to each respective Object via "self". "self" represents the Instance (i.e sammy) NOT the class or its Attributes or Methods.
        self.product_name = product_name
        self.product_price = product_price
        self.product_category = product_category

# ALL METHODS IN PYTHON HAVE TO HAVE "SELF" AS ITS FIRST ATTRIBUTE/PARAMETER, BECAUSE "SELF" IS THE REPRESENTATION OF THE INSTANCE (i.e sammy). Parameters/Attributes are optional with Functions!!! This is a Method that parses and returns (optional/ Also will return None if there is no explicit return statement) a(n) output to the console. And the other two attributes are normal attributes/parameters that take in a String, Integer, List, Dictionary, or any other data type an/or structure. And this Method is for increasing or updating the price for my instance/object.
    def update_price(self, percent_changed, is_increased):
        if is_increased:
            self.product_price *= 1 + percent_changed
            self.print_info()
            return self
        if is_increased == False:
            self.product_price *= 1 - percent_changed
            self.print_info()
            return self

# This is a print_info Method to show the user the information about the product.
    def print_info(self):
        print(f"Product's information: Name - {self.product_name}, Category - {self.product_category}, Price - ${self.product_price}.")
        return self


# Creating Product instances
cucumber = Product("Cucumber", 2.00, "Produce")
tomato = Product("Tomato", 3.00, "Produce")
watermelon = Product("Watermelon",5.99,"Fruit")

# Creating Store Instance
hughes = Store("Reasors")

# Invoking/Calling Product's Methods
cucumber.update_price(1.20, True)
tomato.update_price(0.02, False)

# Invoking/Calling Store's Methods
hughes.add_product(cucumber).print_product().inflation(.20).sell_product(0)
hughes.add_product(tomato)
hughes.print_product()
hughes.inflation(.50)
hughes.sell_product(0)