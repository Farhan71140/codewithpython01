def add_numbers(*args):
    total = sum(args)
    print("Sum:", total)

add_numbers(10, 20, 30)  
# *args → for multiple positional arguments

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Aarav", age=25, city="Hyderabad")
# **kwargs → for multiple keyword arguments


