# Create a set with some duplicate values
my_set = {"apple", "banana", "apple", "cherry"}

# Print the set
print("Set contents:", my_set)  # Duplicates are removed

# Add a new item
my_set.add("orange")
print("After adding orange:", my_set)

# Remove an item
my_set.remove("banana")
print("After removing banana:", my_set)

# Try to access by index (this will cause an error)
# print(my_set[0])  # Sets are unindexed

# Try to change an item (this will cause an error)
# my_set[0] = "grape"  # Sets are immutable