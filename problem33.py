# Question:
# Write a Python program to print the multiplication table of a given number using a while loop.

# Input: Number for which the multiplication table is to be printed
num = int(input("Enter a number to print its multiplication table: "))

# Initialize counter
i = 1

# Print table using while loop from 1 to 10
print(f"\nMultiplication Table of {num}:\n")
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1  # Increment the counter