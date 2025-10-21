# Question:
# Write a Python program to greet all the persons whose names are stored in a list 'l' and start with the letter 's'.

# Sample list of names
l = ["Sana", "Ravi", "Suresh", "Meena", "sam", "Anita", "Steve"]

# Loop through each name in the list
for name in l:
    # Check if the name starts with 's' or 'S'
    if name.lower().startswith('s'):
        print(f"Hello, {name}!")