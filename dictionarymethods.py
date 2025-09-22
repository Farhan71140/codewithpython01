# Create a dictionary
student = {
    "name": "Ravi",
    "age": 20,
    "course": "Math"
}

# .get() method - safely get a value
print("Name:", student.get("name"))       # Output: Ravi
print("Grade:", student.get("grade"))     # Output: None (key doesn't exist)

# .keys() method - get all keys
print("Keys:", student.keys())            # Output: dict_keys(['name', 'age', 'course'])

# .items() method - get all key-value pairs
print("Items:", student.items())          # Output: dict_items([('name', 'Ravi'), ('age', 20), ('course', 'Math')])

# .update() method - add or change values
student.update({"grade": "A", "age": 21}) # Adds 'grade', updates 'age'

# Print updated dictionary
print("Updated Dictionary:", student)