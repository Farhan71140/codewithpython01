# Program to demonstrate logical operators in Python

marks = int(input("Enter your marks out of 100: "))
attendance = int(input("Enter your attendance percentage: "))

# Using logical AND operator
if marks >= 85 and attendance >= 90:
    print("You are eligible for the scholarship! 🎓")
else:
    print("You are not eligible for the scholarship.")

# Using logical OR operator
if marks >= 85 or attendance >= 90:
    print("You meet at least one requirement. 👍")
else:
    print("You meet neither requirement.")

# Using logical NOT operator
if not (marks < 40):
    print("You passed the exam.")
else:
    print("You failed the exam.")