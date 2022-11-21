# Creating the Blueprint or Class
class User:
    # Creating the Constructor or Initiator
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # Deposit Method
    # Takes in the Instance that called it and a single Parameter
    # Similarly Singly Linked List I must return the Object so the Program has the Previous Data and can calculate as expected. Also by returning self the whatever Instance called the Instance Method will now be equal to whatever was calculated in the Function
    def make_deposit(self, amount):
        # Adding to the Instance Attribute via Dereferencing and Parameter
        self.account_balance += amount
        return self
    # Withdrawal Method
    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self
    # Display Account Balance Method
    def display_user_balance(self):
        print(f'User: Name: {self.name}, Balance: {self.account_balance}')
    # Transfer Money Method
    def transfer_money(self,other_user,amount):
        other_user.account_balance += amount
        self.account_balance -= amount
# Off of the Class I am Instantiating Objects
guido = User('Guido van Rossum', 'guido@python.com')
monty = User('Monty Python', 'monty@python.com')
tyson = User('Tyson Smith', 'tyson@pyhton.com')
# Testing that I created the Object and the Initializer work as expected
print(guido.name)
print(monty.name)
print(tyson.name)
# Testing that Chaining Instance Methods work as expected
guido.make_deposit(1000).make_deposit(2000).make_deposit(300).make_withdrawal(500).display_user_balance()
monty.make_deposit(200).make_deposit(250).make_withdrawal(175).make_withdrawal(80).display_user_balance()
tyson.make_deposit(9000).make_withdrawal(300).make_withdrawal(5000).make_withdrawal(100).display_user_balance()
guido.transfer_money(tyson, 5)
guido.display_user_balance()
tyson.display_user_balance()