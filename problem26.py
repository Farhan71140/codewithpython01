# Program to check if a student has passed or failed based on 3 subjects.
# Criteria: Minimum 33% in each subject and 40% overall to pass.

s1 = float(input("Enter marks for Subject 1: "))
s2 = float(input("Enter marks for Subject 2: "))
s3 = float(input("Enter marks for Subject 3: "))
total = s1 + s2 + s3
average = total / 3

if s1 >= 33 and s2 >= 33 and s3 >= 33 and average >= 40:
    print("The student has Passed.")
else:
    print("The student has Failed.")