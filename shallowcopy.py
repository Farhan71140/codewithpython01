# Import the copy module
import copy

# Step 1: Create a nested list (a list of lists)
original = [[1, 2], [3, 4]]

# Step 2: Make a shallow copy of the original list
shallow = copy.copy(original)

# Step 3: Modify the original inner list
original[0][0] = 99

# Step 4: Print both lists to see the effect
print("Original list:", original)
print("Shallow copy :", shallow)