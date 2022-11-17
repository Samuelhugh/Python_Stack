# Python Classes should be PascalCased
class User:
    # This is the Constructor or Initializer, Takes in self with is the newly Instantiated Object and must be provided in the Constructor
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # Deposit Method
    # Takes in self which is the Instance that called upon the Instance Method, and a Parameter for the deposit amount
    def make_deposit(self, amount):
        # The user who called account balance being increases by the amount received from the Parameter
        self.account_balance += amount
    # Withdrawal Method
    def make_withdrawal(self,amount):
        self.account_balance -= amount
    # Displays the user account Printed in one line
    def display_user_balance(self):
        # Python F-String
        print(f'User: Name: {self.name}, Balance: {self.account_balance}')
    def transfer_money(self,other_user,amount):
        # Accessing other_user account balance and adding amount provided from Parameter
        other_user.account_balance += amount
        # Accessing user who transferred money to other_user and subtracting the amount that user transferred
        self.account_balance -= amount
# Off of the User Class/Blueprint I am Instantiating Objects
guido = User('Guido van Rossum', 'guido@python.com')
monty = User('Monty Python', 'monty@python.com')
tyson = User('Tyson Smith', 'tyson@pyhton.com')
# Testing the Constructor via Dereferencing
print(guido.name)
print(monty.name)
print(tyson.name)
# Testing Instance Methods
guido.make_deposit(1000)
guido.make_deposit(2000)
guido.make_deposit(300)
guido.make_withdrawal(500)
guido.display_user_balance()
monty.make_deposit(200)
monty.make_deposit(250)
monty.make_withdrawal(175)
monty.make_withdrawal(80)
monty.display_user_balance()
tyson.make_deposit(9000)
tyson.make_withdrawal(300)
tyson.make_withdrawal(5000)
tyson.make_withdrawal(100)
tyson.display_user_balance()
guido.transfer_money(tyson, 5)
guido.display_user_balance()
tyson.display_user_balance()