# The Module and the File Importing the Module should be in the same Directory
# The "dir" and "help" Functions are handy when exploring Modules
# A Module is a File or Files that are Imported under one Import, A Package is a Collection of Modules in Directories that give a Package Hierarchy
# Namespace refers to which Variables, Functions, and Classes are available to me at any given time during the Program's Execution
# Namespaces are Important to understand because I have to know what Variables I have access to
# To see what Variable are available to me in the namespace I can add the line "print(locals())" in the module that is Importing the Module, What is printed will be a Dictionary where the Variable names are the Keys and the Objects they represent are the Values
# I can use namespace to Control the Functionality that is Imported with the File that Imported the Module
# Whenever I create a File and Execute it, the Python Interpreter automatically creates several Variables
# If multiple Modules utilizes this Module, Local Variables will act as a "Singleton" and will be Initialized only one time
local_val = "magical unicorns"
# Regular Method
def square(x):
    return x * x
# A class named User
class User:
    def __init__(self, name):
        self.name = name
# Instance Method
    def say_hello(self):
        return "hello"
# Testing Regular Method
print(square(5))
# Instantiating a User Object
user = User("Anna")
# Testing the User Initializer
print(user.name)
# Testing the Instance Method
print(user.say_hello())
# This Variable is auto created and assigned a Value
print(__name__)
# If-Check to determine where this File is being Executed from
if __name__ == "__main__":
    print("the file is being executed directly")
else:
    print("The file is being executed because it is imported by another file. The file is called: ", __name__)
# When I Import Modules I don't want to see all the Test Code I wrote, So I can add a Block of Code like this
# if __name__ == "__main__":
#     product = Product([args])
#     print(product)
#     print(product.add_tax(0.18))