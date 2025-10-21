# Question:
# Write a Python program to print the following star pattern:
# ***
# * *
# ***

# Loop through 3 rows
for i in range(1, 4):
    if i == 1 or i == 3:
        print("***")  # First and third rows are solid
    else:
        print("* *")  # Middle row has space in the center