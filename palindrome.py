# Ask the user for input
user_input = input("Enter a word or number: ")

# Remove spaces and convert to lowercase for strings
cleaned = user_input.replace(" ", "").lower()

# Check if it's the same forward and backward
if cleaned == cleaned[::-1]:
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")