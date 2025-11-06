'''Create a class BankAccount with private attribute __balance. Add methods deposit() and 
get_balance() to safely access and modify the balance.'''
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

# Create account object
acc = BankAccount(1000)

# Deposit money
acc.deposit(500)

# Check balance
print("Balance:", acc.get_balance())  # Output: Balance: 1500