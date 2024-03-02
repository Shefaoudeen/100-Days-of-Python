# importing the required libraries and modules
import os
import random
import art
import game_data


def random_choice():
    """Pick a random dict from the data"""
    return random.choice(game_data.data)


def printLogo():
    """Print the logo"""
    os.system('cls')
    print(art.logo)


def declare(score):
    """Declare the score"""
    printLogo()
    print(f"Sorry, that's wrong, Final score: {score}")


def printCompare(data1, data2):
    """Print the compare strings"""
    print(
        f"Compare A: {data1['name']}, {data1['description']}, from {data1['country']}")
    print(art.vs)
    print(
        f"Compare B: {data2['name']}, {data2['description']}, from {data2['country']}")
    guess = input("Who has more followers? Type 'A' or 'B' : ").lower()
    return guess


def higherLower():
    """Higher Lower game"""

    score = 0
    game_over = False

    printLogo()
    data1 = random_choice()
    data2 = random_choice()
    guess = printCompare(data1, data2)

    while not game_over:
        if data1['follower_count'] > data2['follower_count'] and guess == 'b':
            declare(score)
            game_over = True

        elif data2['follower_count'] > data1['follower_count'] and guess == 'a':
            declare(score)
            game_over = True

        else:
            printLogo()
            score += 1

            print(f"Your current score : {score}")

            if data1['follower_count'] < data2['follower_count']:
                data1 = data2

            data2 = random_choice()
            while data1 == data2:
                data2 = random_choice()
            guess = printCompare(data1, data2)


higherLower()
