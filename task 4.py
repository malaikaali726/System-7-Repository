# Task 4: Bank Account class with methods

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return
        if amount > self.balance:
            print("Insufficient balance. Withdrawal not possible.")
            return
        self.balance -= amount
        print(f"{amount} withdrawn. New balance: {self.balance}")

    def show_balance(self):
        print(f"{self.owner}'s balance: {self.balance}")


if __name__ == "__main__":
    account = BankAccount("Laina", 1000)
    account.show_balance()
    account.deposit(500)
    account.withdraw(200)
    account.withdraw(5000)
    account.show_balance()