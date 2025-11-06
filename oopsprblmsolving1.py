#Method That Updates Multiple Attributes
'''Question
Create a class Account with attributes name, balance. Add a method deposit(amount) that increases the balance and prints the new balance.'''

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name}'s new balance is ₹{self.balance}")

# Create an account object
acc1 = Account("Farhan", 5000)

# Deposit money
acc1.deposit(1500)  # Output: Farhan's new balance is ₹6500