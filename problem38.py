# Question:
# Write a Python program to print the multiplication table of a given number n using for loops in reversed order.

# Input: Number for which the multiplication table is to be printed
n = int(input("Enter a number to print its multiplication table in reverse order: "))

# Loop from 10 down to 1
print(f"\nReversed Multiplication Table of {n}:\n")
for i in range(10, 0, -1):
    print(f"{n} x {i} = {n * i}")