# Simple program to demonstrate if, elif, and else

age = int(input("Enter your age: "))

if age < 5:
    print("You get a free ticket! 🎟️")
elif age < 13:
    print("You qualify for a child ticket.")
elif age < 60:
    print("You qualify for an adult ticket.")
else:
    print("You qualify for a senior citizen ticket.")