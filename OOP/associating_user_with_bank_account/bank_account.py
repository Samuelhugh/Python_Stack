# Defining the Blueprint or Class
class BankAccount:
# Class Variable
    users = []
# Constructor, Must include self, Also using Default values
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
        print(f'Balance: ${self.balance}')
        return self
    
    def yield_interest(self):
        if self.balance >= 0:
            self.balance *= 1 + self.int_rate
            # This also works
            # self.balance = self.balance * (1 + self.int_rate)
        return self
# Class Method, Must provide cls
    @classmethod
    def display_all_users(cls):
        for x in cls.users:
            x.display_account_info()
# Off of the class I Instantiated 2 Objects
sam = BankAccount()
tyson = BankAccount()
# Instance Method Testing
sam.deposit(15).withdraw(7).withdraw(3)
sam.yield_interest()
# Class Method Testing
BankAccount.display_all_users()