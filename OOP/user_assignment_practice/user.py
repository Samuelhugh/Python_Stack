class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
    def make_withdrawal(self,amount): # the withdrawal for a specific user's account
        self.account_balance -= amount
    def display_user_balance(self): # the display of the user's name and account balance printed in one line
        print(f'User: Name: {self.name}, Balance: {self.account_balance}')
    def transfer_money(self,other_user,amount):
        other_user.account_balance += amount
        self.account_balance -= amount
guido = User('Guido van Rossum', 'guido@python.com')
monty = User('Monty Python', 'monty@python.com')
tyson = User('Tyson Smith', 'tyson@pyhton.com')
print(guido.name)	# output: Guido van Rossum
print(monty.name)
print(tyson.name)
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