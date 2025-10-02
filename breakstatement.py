# A list of numbers
numbers = [10, 20, 30, 40, 50]

# We want to find number 30
for num in numbers:
    print("Checking number:", num)  # Show which number we're checking
    if num == 30:
        print("Found 30! Stopping the loop.")
        break  # Exit the loop when 30 is found

    #the break statement is used to stop a loop early—before it finishes all its iterations.
#It’s like saying: “Okay, I found what I need—let’s exit the loop now!”
