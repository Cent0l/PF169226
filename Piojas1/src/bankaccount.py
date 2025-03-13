class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self,amount):
        if amount<0:
            raise ValueError("Deposit cannot be lower than 0")
        self.balance+=amount

    def withdraw(self, amount):
        if amount<0:
            raise ValueError("Withdraw cannot be lower than 0")
        if amount>self.balance:
            raise ValueError("Not enough money")
        self.balance-=amount

    def get_balance(self):
        return self.balance
