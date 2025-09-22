# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "age": 30  # Duplicate key; this will overwrite the previous 'age' value
}

# ✅ Dictionaries are mutable: we can change values
my_dict["city"] = "Los Angeles"

# ✅ Dictionaries are indexed by keys
print("Name:", my_dict["name"])  # Accessing value using key

# ✅ Dictionaries cannot have duplicate keys
# Only the last 'age' key-value pair is retained
print("Age:", my_dict["age"])

# ✅ Dictionaries are unordered (prior to Python 3.7)
# But from Python 3.7+, they maintain insertion order
print("Full Dictionary:")
for key, value in my_dict.items():
    print(f"{key}: {value}")