# Create two sets
set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "orange", "grape"}

# 1. Length of a set
print("Length of set1:", len(set1))

# 2. Remove an item from set1
set1.remove("banana")
print("After removing 'banana' from set1:", set1)

# 3. Pop an item from set1 (removes a random item)
popped_item = set1.pop()
print("Popped item:", popped_item)
print("Set1 after pop:", set1)

# 4. Clear all items from set2
set2.clear()
print("Set2 after clearing:", set2)

# Create new sets for union and intersection
a = {"red", "green", "blue"}
b = {"green", "yellow", "blue"}

# 5. Union of sets
union_set = a.union(b)
print("Union of a and b:", union_set)

# 6. Intersection of sets
intersection_set = a.intersection(b)
print("Intersection of a and b:", intersection_set)