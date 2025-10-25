# Recursive function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1  # Base case
    return n * factorial(n - 1)  # Recursive call

# Recursive function to calculate nth Fibonacci number
def fibonacci(n):
    if n <= 0:
        return 0  # Base case
    elif n == 1:
        return 1  # Base case
    return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive call

# Recursive function to reverse a string
def reverse_string(s):
    if len(s) == 0:
        return s  # Base case
    return reverse_string(s[1:]) + s[0]  # Recursive call

# Recursive function to sum elements of a list
def sum_list(lst):
    if len(lst) == 0:
        return 0  # Base case
    return lst[0] + sum_list(lst[1:])  # Recursive call

# Recursive function to check if a number is a palindrome
def is_palindrome(num_str):
    if len(num_str) <= 1:
        return True  # Base case
    if num_str[0] != num_str[-1]:
        return False
    return is_palindrome(num_str[1:-1])  # Recursive call

# Driver code to test all functions
if __name__ == "__main__":
    print("Factorial of 5:", factorial(5))
    print("Fibonacci of 6:", fibonacci(6))
    print("Reverse of 'hello':", reverse_string("hello"))
    print("Sum of [1, 2, 3, 4]:", sum_list([1, 2, 3, 4]))
    print("Is '121' a palindrome?", is_palindrome("121"))