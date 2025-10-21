# Question:
# Write a Python program using functions to find the greatest of three numbers.

# Define the function
def find_greatest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Input: Get three numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Call the function and display the result
greatest = find_greatest(num1, num2, num3)
print(f"\nThe greatest of the three numbers is: {greatest}")