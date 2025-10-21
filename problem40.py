# Question:
# Write a Python program using a function to convert Celsius to Fahrenheit.

# Define the conversion function
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Input: Get temperature in Celsius from the user
c = float(input("Enter temperature in Celsius: "))

# Call the function and display the result
f = celsius_to_fahrenheit(c)
print(f"\n{c}°C is equal to {f}°F")