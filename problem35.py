# Question:
# Write a Python program to print the following star pattern: *, ***, ***** for n = 3

# Input: Number of lines
n = 3

# Loop to print each line
for i in range(1, n + 1):
    stars = 2 * i - 1  # Calculate number of stars for each line
    print("*" * stars)