class BankAccount:

    users = []

    def __init__(self, int_rate=0.01, balance=0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.users.append(self)
        # print(self.int_rate)
    
    def deposit(self, amount):
        self.balance += amount
        # print(self.balance, amount)
        return self
    
    def withdraw(self, amount):
        self.balance -= amount
        # print(self.balance, amount)
        if self.balance < 0:
            print('Insufficient funds: Charging a $5 Fee')
            self.balance -= 5
        return self
            # print(self.balance, amount)
    
    def display_account_info(self):
        return f'${self.balance}'
    
    def yield_interest(self):
        if self.balance >= 0:
            self.balance *= 1 + self.int_rate
        return self
    
    @classmethod
    def display_all_users(cls):
        for x in cls.users:
            x.display_account_info()
class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {'checking' : BankAccount(0.02,4000), 'savings' : BankAccount(0.05,3000)}
    def display_user_balance(self):
        print(f"User: {self.name}, Checking Balance: {self.account['checking'].display_account_info()}")
        print(f"User: {self.name}, Savings Balance: {self.account['savings'].display_account_info()}")
        return self
    def transfer_money(self,other_user,amount):
        other_user.account += amount
        self.account -= amount
        self.display_user_balance()
        other_user.display_user_balance()
        return self
sam = User('sam','sam')
tyson = User('tyson','tyson')
sam.account['checking'].deposit(100)
sam.display_user_balance()