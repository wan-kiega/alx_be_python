# bank_account.py

class BankAccount:
    def __init__(self, account_balance=0.0):
        self.account_balance = float(account_balance)

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += float(amount)
            return True
        return False

    def withdraw(self, amount):
        amount = float(amount)
        if amount <= 0:
            print("Amount must be greater than zero.")
            return False
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            print("Insufficient funds.")
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")

# main-0.py

import sys
from bank_account import BankAccount 

def main():
    initial_balance = float(sys.argv[1]) if len(sys.argv) > 1 else 0.0
    account = BankAccount(initial_balance)

    if len(sys.argv) < 3:
        account.display_balance()
        return

    operation = sys.argv[2].lower()

    if operation == "deposit" and len(sys.argv) == 4:
        amount = float(sys.argv[3])
        account.deposit(amount)
        account.display_balance()
    elif operation == "withdraw" and len(sys.argv) == 4:
        amount = float(sys.argv[3])
        success = account.withdraw(amount)
        if success:
            print(f"Withdrew ${amount:.2f}")
        account.display_balance()
    elif operation == "balance":
        account.display_balance()
    else:
        print("Usage:")
        print("python main-0.py [initial_balance] [operation] [amount]")
        print("Operations: deposit, withdraw, balance")

if __name__ == "__main__":
    main()