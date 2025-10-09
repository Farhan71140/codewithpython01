# INTEGER with WHILE loop
print("WHILE loop with INTEGER:")
num = 1
while num <= 3:
    print("Integer value:", num)  # Prints 1, 2, 3
    num += 1

# FLOAT with WHILE loop
print("\nWHILE loop with FLOAT:")
price = 1.0
while price < 2.0:
    print("Float value:", round(price, 2))  # Prints 1.0, 1.3, 1.6, 1.9
    price += 0.3

# STRING with FOR loop
print("\nFOR loop with STRING:")
text = "loop"
for char in text:
    print("Character:", char)  # Prints each letter in "loop"

# LIST with FOR loop
print("\nFOR loop with LIST:")
colors = ["red", "green", "blue"]
for color in colors:
    print("Color:", color)

# TUPLE with FOR loop
print("\nFOR loop with TUPLE:")
dimensions = (10, 20, 30)
for dim in dimensions:
    print("Dimension:", dim)

# SET with FOR loop
print("\nFOR loop with SET:")
unique_numbers = {1, 2, 3}
for number in unique_numbers:
    print("Unique number:", number)

# DICTIONARY with FOR loop
print("\nFOR loop with DICTIONARY:")
person = {"name": "Alice", "age": 25}
for key, value in person.items():
    print(key, ":", value)