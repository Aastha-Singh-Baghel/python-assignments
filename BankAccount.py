class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    # Method to deposit money
    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    # Method to withdraw money
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    # Method to check balance
    def check_balance(self):
        print("Current Balance:", self.balance)


# Creating an object of the class
account = BankAccount("12345", 1000)

# Using methods
account.deposit(500)
account.withdraw(300)
account.check_balance()
