# Defining the Class
class BankAccount:
# Class Variable
    users = []
# Initializer Method
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.users.append(self)
# Instance Methods
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance - amount < 0:
            print('Insufficient Funds: Charging a $5 Fee')
            self.balance -= 5
            return self
        else:
            self.balance -= amount
            return self
    
    def display_account_info(self):
        return f'${self.balance}'
    
    def yield_interest(self):
        if self.balance >= 0:
            self.balance *= 1 + self.int_rate
            # This also works
            # self.balance = self.balance * (1 + self.int_rate)
        return self
# Class Method
    @classmethod
    def display_all_users(cls):
        for x in cls.users:
            x.display_account_info()

# Defining User Blueprint within the same Script
class User:
# Initializer Method
    def __init__(self, name, email):
        self.name = name
        self.email = email
        # Every newly Instantiated Object will be Associated with a account via the BankAccount Class
        self.checking = BankAccount(int_rate = 0.02,balance = 4000)
        self.savings = BankAccount(int_rate = 0.02,balance = 8000)
    # Displaying the Account Balance off of the User Instance
    def display_user_balance(self):
        print(f"User: {self.name}, Checking Balance: {self.checking.display_account_info()}")
        print(f"User: {self.name}, Savings Balance: {self.savings.display_account_info()}")
        return self
    # Allowing Transfer of money off of the User Instance
    def transfer_money(self,other_user,amount):
        self.checking.balance -= amount
        other_user.checking.balance += amount
        # self.display_user_balance()
        # other_user.display_user_balance()
        return self
# Off of the User Class I am Instantiating 2 Objects
sam = User('sam','sam@s.com')
tyson = User('tyson','tyson@t.com')
# User Instance Methods Testing
sam.display_user_balance()
tyson.display_user_balance()
sam.transfer_money(tyson,50)
sam.display_user_balance()
sam.savings.deposit(150)
sam.display_user_balance()
sam.checking.deposit(900)
sam.display_user_balance()
# print(sam.email)