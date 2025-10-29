import random

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'snake' and computer == 'water') or \
         (user == 'water' and computer == 'gun') or \
         (user == 'gun' and computer == 'snake'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    choices = ['snake', 'water', 'gun']
    print("Welcome to Snake-Water-Gun Game!")
    print("Type 'snake', 'water', or 'gun' to play. Type 'exit' to quit.")

    while True:
        user_choice = input("Your choice: ").lower()
        if user_choice == 'exit':
            print("Thanks for playing!")
            break
        if user_choice not in choices:
            print("Invalid choice. Try again.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)

play_game()