# Program to check whether a given username contains less than 10 characters

username = input("Enter your username: ")
if len(username) < 10:
    print("Username contains less than 10 characters.")
else:
    print("Username has 10 or more characters.")