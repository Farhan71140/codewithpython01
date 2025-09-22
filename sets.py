# Creating sets
fruits = {"apple", "banana", "cherry"}
vegetables = {"carrot", "broccoli", "banana"}

# Displaying the sets
print("Fruits:", fruits)
print("Vegetables:", vegetables)

# Adding an item to a set
fruits.add("orange")
print("Fruits after adding orange:", fruits)

# Removing an item from a set
fruits.remove("apple")
print("Fruits after removing apple:", fruits)

# Set operations
print("Common items (intersection):", fruits & vegetables)
print("All items (union):", fruits | vegetables)
print("Items in fruits but not in vegetables (difference):", fruits - vegetables)

# Checking membership
print("Is 'banana' in fruits?", "banana" in fruits)