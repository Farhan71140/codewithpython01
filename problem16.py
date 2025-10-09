# Question: Write a program to sum a list with 4 numbers.

numbers = []  # Create an empty list to store numbers

for i in range(4):  # Loop to get 4 numbers from the user
    num = float(input(f"Enter number {i+1}: "))  # Take input and convert to float
    numbers.append(num)  # Add the number to the list

total = sum(numbers)  # Calculate the sum of the list

print("The sum of the numbers is:", total)  # Display the result