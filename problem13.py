# Question: Write a program to store seven fruits in a list entered by the user.

# Create an empty list
fruits = []

# Ask the user to enter 7 fruits
for i in range(7):
    fruit = input("Enter the name of a fruit: ")
    fruits.append(fruit)

# Print the list of fruits
print("Fruits you entered:", fruits)