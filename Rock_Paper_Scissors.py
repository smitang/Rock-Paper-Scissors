# Author: Stephen Tang
# Date: 12/1/2021
# Description: This is a game between the computer and a player. The computer will randomly choose rock, paper or
# scissor while the player will choose one of the three options as well. The rules of rock, paper, scissor will be used
# to determine the outcome of the choices - win, lose, draw. After the output is displayed, The player will be asked
# whether to keep playing or to quit.

while True:
    import random
    computer_choice = random.choice(range(0, 3))
    player_choice = int(input('''
        Welcome to Rock, Paper, Scissors
        Please enter a number to select your choice:
                (0) Rock
                (1) Paper
                (2) Scissor
    '''))
    if player_choice == 0 and computer_choice == 0:                                         # Player chooses 0 (Rock)
        print("Tie Game: Player chose Rock. Computer chose Rock.")                              # Draw
        play_again = input("Would you like to play again? Enter 'Y' if Yes or 'N' if No: ").upper()
        if play_again == 'N':
            print("Thank you for playing Rock, Paper, Scissors!")
            break
    if player_choice == 0 and computer_choice == 1:                                             # Computer Wins
        print("Computer Wins: Player chose Rock. Computer chose Paper.")
        play_again = input("Would you like to play again? Enter 'Y' if Yes or 'N' if No: ").upper()
        if play_again == 'N':
            print("Thank you for playing Rock, Paper, Scissors!")
            break
    if player_choice == 0 and computer_choice == 2:                                             # Player wins
        print("Player Wins: Player chose Rock. Computer chose Scissors.")
        play_again = input("Would you like to play again? Enter 'Y' if Yes or 'N' if No: ").upper()
        if play_again == 'N':
            print("Thank you for playing Rock, Paper, Scissors!")
            break
    if player_choice == 1 and computer_choice == 1:                                       # Player chooses 1 (Paper)
        print("Tie Game: Player chose Paper. Computer chose Paper.")                            # Draw
        play_again = input("Would you like to play again? Enter 'Y' if Yes or 'N' if No: ").upper()
        if play_again == 'N':
            print("Thank you for playing Rock, Paper, Scissors!")
            break
    if player_choice == 1 and computer_choice == 2:                                             # Computer Wins
        print("Computer Wins: Player chose Paper. Computer chose Scissors.")
        play_again = input("Would you like to play again? Enter 'Y' if Yes or 'N' if No: ").upper()
        if play_again == 'N':
            print("Thank you for playing Rock, Paper, Scissors!")
            break
    if player_choice == 1 and computer_choice == 0:                                             # Player Wins
        print("Player Wins: Player chose Paper. Computer chose Rock.")
        play_again = input("Would you like to play again? Enter 'Y' if Yes or 'N' if No: ").upper()
        if play_again == 'N':
            print("Thank you for playing Rock, Paper, Scissors!")
            break
    if player_choice == 2 and computer_choice == 2:                                      # Player chooses 3 (Scissors)
        print("Tie Game: Player chose Scissors. Computer chose Scissors.")                        # Draw
        play_again = input("Would you like to play again? Enter 'Y' if Yes or 'N' if No: ").upper()
        if play_again == 'N':
            print("Thank you for playing Rock, Paper, Scissors!")
            break
    if player_choice == 2 and computer_choice == 0:                                             # Computer Wins
        print("Computer Wins: Player chose Scissors. Computer chose Rock.")
        play_again = input("Would you like to play again? Enter 'Y' if Yes or 'N' if No: ").upper()
        if play_again == 'N':
            print("Thank you for playing Rock, Paper, Scissors!")
            break
    if player_choice == 2 and computer_choice == 1:                                             # Player wins
        print("Player Wins: Player chose Scissors. Computer chose Paper.")
        play_again = input("Would you like to play again? Enter 'Y' if Yes or 'N' if No: ").upper()
        if play_again == 'N':
            print("Thank you for playing Rock, Paper, Scissors!")
            break
