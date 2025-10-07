# Question: Write a program to input eight numbers from the user and display all the unique numbers (once).

numbers = []  # Create an empty list to store the numbers

for i in range(8):  # Loop to get 8 numbers from the user
    num = int(input(f"Enter number {i+1}: "))  # Take input and convert to integer
    numbers.append(num)  # Add the number to the list

unique_numbers = set(numbers)  # Convert the list to a set to remove duplicates

print("Unique numbers entered:", unique_numbers)  # Display the unique numbers