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
        return self
        if self.balance < 0:
            print('Insufficient funds: Charging a $5 Fee')
            self.balance -= 5
            # print(self.balance, amount)
    
    def display_account_info(self):
        print(f'Balance: ${self.balance}')
        return self
    
    def yield_interest(self):
        if self.balance >= 0:
            self.balance *= 1 + self.int_rate
        return self
    
    @classmethod
    def display_all_users(cls):
        for x in cls.users:
            x.display_account_info()
sam = BankAccount()
tyson = BankAccount()