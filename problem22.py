# Create an empty dictionary and allow 4 friends to enter their favorite programming language using their names as unique keys

# Initialize an empty dictionary
favorite_languages = {}

# Collect input from 4 friends
for i in range(4):
    name = input(f"Enter name of friend {i+1}: ")
    language = input(f"Enter {name}'s favorite programming language: ")
    favorite_languages[name] = language

# Display the final dictionary
print("\nFavorite Languages Dictionary:")
print(favorite_languages)