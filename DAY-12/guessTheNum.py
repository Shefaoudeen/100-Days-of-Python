# importing the required libraries and modules
import art
import random
import os


def guessTheNumber(difficulty):
    """Guess the Number game"""
    # assign lives
    lives = 0
    if difficulty == "easy":
        lives = 10
    elif difficulty == "hard":
        lives = 5

    # assign the random number
    random_Number = random.randint(1, 100)
    player_won = False

    # play until guess is correct or run out of lives
    while not player_won and lives > 0:
        print(f"You have {lives} attempts remaining to guess the number")
        guess = int(input("Make a guess : "))
        if guess == random_Number:
            print("You Won")
            player_won = True
        elif guess > random_Number:
            print("Too high")
            lives -= 1
        elif guess < random_Number:
            print("Too low")
            lives -= 1

    if lives == 0:
        print(f"You Lose, the correct number is {random_Number}")


os.system('cls')
print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a Number between 1 and 100.")
difficulty = input("Choose a difficulty.Type 'easy' or 'hard': ").lower()
guessTheNumber(difficulty)
