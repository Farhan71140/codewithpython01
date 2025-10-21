# Question:
# Write a Python program to print the multiplication table of a given number using a for loop.

# Input: Number for which the multiplication table is to be printed
num = int(input("Enter a number to print its multiplication table: "))

# Using a for loop to generate and print the table from 1 to 10
print(f"\nMultiplication Table of {num}:\n")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")