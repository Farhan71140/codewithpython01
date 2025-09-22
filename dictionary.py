# Creating a dictionary of fruits and their colors
fruit_colors = {
    "apple": "red",
    "banana": "yellow",
    "grape": "purple",
    "orange": "orange"
}

# Accessing a value using a key
print("The color of banana is:", fruit_colors["banana"])

# Adding a new key-value pair
fruit_colors["kiwi"] = "green"

# Updating a value
fruit_colors["apple"] = "greenish-red"

# Removing a key-value pair
del fruit_colors["grape"]

# Looping through the dictionary
for fruit, color in fruit_colors.items():
    print(f"{fruit.capitalize()} is {color}")