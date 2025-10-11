# Create an empty dictionary and allow 4 friends to enter their favorite programming language using their names as unique keys.
# What if the names of 2 friends are the same? In that case, the dictionary will overwrite the previous entry with the new one,
# because dictionary keys must be unique. So only the last entered value for that name will be stored.

# Initialize an empty dictionary
favorite_languages = {}

# Collect input from 4 friends
for i in range(4):
    name = input(f"Enter name of friend {i+1}: ")
    language = input(f"Enter {name}'s favorite programming language: ")
    favorite_languages[name] = language  # If name already exists, this will overwrite the previous value

# Display the final dictionary
print("\nFavorite Languages Dictionary:")
print(favorite_languages)