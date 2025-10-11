# Program to calculate the grade of a student based on marks.
# Grading Scheme:
# 90–100 => Excellent
# 80–90  => A Grade
# 70–80  => B Grade
# 60–70  => C Grade
# 50–60  => D Grade
# Below 50 => Fail

marks = float(input("Enter the student's marks (out of 100): "))

if 90 <= marks <= 100:
    print("Grade: Excellent")
elif 80 <= marks < 90:
    print("Grade: A Grade")
elif 70 <= marks < 80:
    print("Grade: B Grade")
elif 60 <= marks < 70:
    print("Grade: C Grade")
elif 50 <= marks < 60:
    print("Grade: D Grade")
elif 0 <= marks < 50:
    print("Grade: Fail")
else:
    print("Invalid marks entered.")