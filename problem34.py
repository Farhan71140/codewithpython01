# Question:
# Write a Python program to find the sum of the first n natural numbers using a while loop.

# Input: Get the value of n from the user
n = int(input("Enter a positive integer n: "))

# Initialize counter and sum
i = 1
total = 0

# Loop to add numbers from 1 to n
while i <= n:
    total += i  # Add current number to total
    i += 1      # Move to the next number

# Output the result
print(f"\nSum of the first {n} natural numbers is: {total}")