# Question: Write a program to create a dictionary of Hindi words with values as their English translation and provide user with an option to look it up.

translations = {  # Dictionary of Hindi words (spelled in English) and their English meanings
    "chand": "moon",       # 'chand' means 'moon'
    "suraj": "sun",        # 'suraj' means 'sun'
    "pani": "water",       # 'pani' means 'water'
    "kitab": "book",       # 'kitab' means 'book'
    "ghar": "house",       # 'ghar' means 'house'
    "ped": "tree",         # 'ped' means 'tree'
    "aasman": "sky"        # 'aasman' means 'sky'
}

print("Available Hindi words:", list(translations.keys()))  # Show the list of available Hindi words

word = input("Enter a Hindi word (spelled in English): ")  # Ask the user to enter a Hindi word

if word in translations:  # Check if the word exists in the dictionary
    print(f"The English translation of '{word}' is '{translations[word]}'")  # Show the translation
else:
    print(f"Sorry, the word '{word}' is not in the dictionary.")  # Show error if word not found