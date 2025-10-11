# Program to detect spam comments.
# A comment is considered spam if it contains any of the following keywords:
# "make a lot of money", "buy now", "subscribe this", "click this"

spam_keywords = [
    "make a lot of money",
    "buy now",
    "subscribe this",
    "click this"
]

comment = input("Enter the comment: ").lower()
if any(keyword in comment for keyword in spam_keywords):
    print("This is a spam comment.")
else:
    print("This comment is not spam.")