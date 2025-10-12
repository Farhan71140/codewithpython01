# Ask the user how many terms they want
n = int(input("Enter the number of terms: "))

# First two Fibonacci numbers
a, b = 0, 1

# Counter
count = 0

# Print Fibonacci series
print("Fibonacci Series:")
while count < n:
    print(a, end=" ")
    a, b = b, a + b  # Update values
    count += 1