"""
🧾 Question:
Create a CustomString class that:
- Accepts a string on initialization
- Has methods to return:
  - Uppercase
  - Lowercase
  - Title case
  - Reversed string
- Challenge: Add a method to check if the string is a palindrome
"""

class CustomString:
    def __init__(self, text):
        self.text = text

    def to_uppercase(self):
        return self.text.upper()

    def to_lowercase(self):
        return self.text.lower()

    def to_titlecase(self):
        return self.text.title()

    def reverse_string(self):
        return self.text[::-1]

    def is_palindrome(self):
        cleaned = self.text.replace(" ", "").lower()
        return cleaned == cleaned[::-1]


# 🧪 Sample Usage
if __name__ == "__main__":
    s = CustomString("Madam")
    print("Original:", s.text)
    print("Uppercase:", s.to_uppercase())
    print("Lowercase:", s.to_lowercase())
    print("Title Case:", s.to_titlecase())
    print("Reversed:", s.reverse_string())
    print("Is Palindrome:", s.is_palindrome())