# Loop through numbers from 1 to 5
for num in range(1, 6):
    if num == 3:
        continue  # Skip the rest of the loop when num is 3
    print("Number is:", num)  # This line won't run when num is 3

   #The loop goes through numbers 1 to 5.
#When it reaches 3, the continue statement tells Python to skip the rest of the loop just for that round.
# So print() is not called when num is 3.
# The loop then continues with the next number.
