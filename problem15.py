# Question: Check that a tuple type cannot be changed in Python.

my_tuple = (10, 20, 30)  # Create a tuple with three elements
print("Original tuple:", my_tuple)

# Try to change the first element
try:
    my_tuple[0] = 99  # Attempt to modify the tuple
except TypeError as e: #- This catches a specific type of error — in this case, a TypeError. A TypeError occurs when an operation is applied to an object of inappropriate type (like trying to change a tuple, which is immutable).
    print("Error:", e)  # This will print a TypeError