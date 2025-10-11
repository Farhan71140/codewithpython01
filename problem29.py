# Program to check whether a given name is present in a list or not

names = ["Alice", "Bob", "Charlie", "David", "Farhan"]
name_to_check = input("Enter a name to search: ")

if name_to_check in names:
    print(f"{name_to_check} is present in the list.")
else:
    print(f"{name_to_check} is not present in the list.")