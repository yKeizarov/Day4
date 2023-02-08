# Project: Rock, Paper, Scissors
import pictures as pc
import random

choice_list = ["rock", "paper", "scissors"]


def game():
    computer_choice = random.randrange(1, 4)
    user_choice = input("Your choice is:  ").lower()
    if user_choice in choice_list:
        if computer_choice == 1:
            if user_choice == 'rock':
                print(f"It's DRAW. User {pc.ROCK} vs computer {pc.ROCK}")
                return 0
            elif user_choice == "paper":
                print(f"It's WIN. User {pc.PAPER} vs computer {pc.ROCK}")
                return 1
            else:
                print(f"You are LOSE. User {pc.SCISSORS} vs computer {pc.ROCK}")
                return 2
        if computer_choice == 2:
            if user_choice == 'rock':
                print(f"You are LOSE. User {pc.ROCK} vs computer {pc.PAPER}")
                return 2
            elif user_choice == "paper":
                print(f"It's DRAW. User {pc.PAPER} vs computer {pc.PAPER}")
                return 0
            else:
                print(f"You WIN. User {pc.SCISSORS} vs computer {pc.PAPER}")
                return 1
        if computer_choice == 3:
            if user_choice == 'rock':
                print(f"You WIN. User {pc.ROCK} vs computer {pc.SCISSORS}")
                return 1
            elif user_choice == "paper":
                print(f"You are LOSE. User {pc.PAPER} vs computer {pc.SCISSORS}")
                return 2
            else:
                print(f"It's DRAW. User {pc.SCISSORS} vs computer {pc.SCISSORS}")
                return 0
    else:
        print("Please, choice around: ROCK, PAPER or SCISSORS. ")
        return 404


game_status = True
user_count = 0
computer_count = 0


if __name__ == '__main__':
    print("Welcome to game.")
    while game_status:
        result = game()
        if result == 0 or result == 1 or result == 2:
            if result == 1:
                user_count += 1
            elif result == 2:
                computer_count += 1
            elif result == 0:
                user_count = user_count
                computer_count = computer_count
            else:
                pass

            control_question = int(input(f"Now result: USER-{user_count} vs COMPUTER-{computer_count}. "
                                     f"Do you play again? 1 - YES, 2 - NO. "))
            if control_question == 1 or control_question == 2:
                if control_question == 2:
                    if user_count > computer_count:
                        print(f"Final result: USER-{user_count} vs COMPUTER-{computer_count}. "
                              f"Congratulations, YOU WIN!")
                        game_status = False
                    elif user_count < computer_count:
                        print(f"Final result: USER-{user_count} vs COMPUTER-{computer_count}. "
                              f"YOU LOSE...")
                        game_status = False
                    elif user_count == computer_count:
                        print(f"Final result: USER-{user_count} vs COMPUTER-{computer_count}. "
                              f"Congratulations, IT'S DRAW!")
                        game_status = False
            else:
                control_question = input("Your choice is incorrect. Please make the right choice. ")
                continue
        else:
            continue
