"""
Rock, Paper and scissors command line game
player vs computer

"""
import random

def get_computer_choice():
    """ return a randomn choise from rock, paper and scissors. """
    return random.choice(['rock', 'paper', 'scissors'])


def get_users_choice():
    """
    prompt the user for their choise.
    varidate input (case sensitive strip whotespace)
    repeat untill a valid choise is entered
    """

    valid_choices = {'rock', 'paper', 'scissors'}
    while True:
        user_input = input("\nEnter rock, paper or scissors:").strip().lower()

        if user_input in valid_choices:
            return user_input

        else:
            print("invalid choice, please type  'rock', 'paper', or 'scissors'.")

def determine_winner(user_choice, computer_choice):
    """
    Determine the winner based on the predefined rules
     return a dtring based on  the outcome.
    """

    if user_choice == computer_choice:
        return "it s a tie"

    #winning condations
    if (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice ==  "paper") or (user_choice == "paper" and computer_choice == "rock"):

        return "you win"

    else:
        return "computer wins"

def main():
    """main game loop"""
    print("welcome to the  Rock Scissors and Rock game!")
    print("."*20)
    while True:
        #get users choise
        user_choice = get_users_choice()
        computer_choice = get_computer_choice()
 
        print(f"\nyou chose: {user_choice}")
        #display rthw winner
        result = determine_winner(user_choice, computer_choice)
        print(result)

        #ask use if they want to play again
    
        play_again = input("\ndo you want to play again? (y/n):").strip().lower()

        if play_again != "y":
            print("thanks for playing! goog bye.")

            break


if __name__ == "__main__":
    main()
 
