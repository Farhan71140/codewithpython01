# A list of numbers
numbers = [1, 3, 5, 7, 9]

# We want to check if number 4 is in the list
for num in numbers:
    if num == 4:
        print("Found number 4!")
        break  # Stop the loop if 4 is found
else:
    print("Number 4 was not found in the list.")