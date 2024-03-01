# importing necessary libraries and modules
import art
import os
import random

# generate cards


def generate_card(player_cards):
    """Generate random cards in the person's deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    if random_card == 11:
        if sum(player_cards) > 10:
            random_card -= 10
    player_cards.append(random_card)

# decides continuous


def ask_continue():
    """Ask the willingness of the player to continue the game"""
    draw_next = input("Type 'y' to get another card, type 'n' to pass: ")
    if draw_next == 'y':
        return True
    return False

# decide the winner


def declare(player_card, opponent_card):
    """Decides who is the winner"""
    player_total = sum(player_card)
    oppoent_total = sum(opponent_card)

    print(f"Your final hand: {player_card}, final score: {player_total}")
    print(
        f"Computer final hand: {opponent_card}, final score: {oppoent_total} \n")

    if player_total <= 21:
        if oppoent_total > 21:
            print("You Win")
        elif player_total > oppoent_total:
            print("You Win")
        elif player_total == oppoent_total:
            print("Match Draw")
        else:
            print("You Lose")
    else:
        print("You Lose")

# actual game


def blackJack():
    """BlackJack game"""
    os.system('cls')
    print(art.logo)

    player_card = []
    opponent_card = []

    for _ in range(2):
        generate_card(player_card)

    for _ in range(2):
        generate_card(opponent_card)

    print(f"Your cards: {player_card}, current score: {sum(player_card)}")
    print(f"Computer's first card: {opponent_card[0]}")

    willing = True

    while sum(player_card) < 17 or willing:
        while willing:
            if sum(player_card) >= 21:
                declare(player_card, opponent_card)
            willing = ask_continue()
            if willing:
                generate_card(player_card)
                print(
                    f"Your cards: {player_card}, current score: {sum(player_card)}")
            else:
                if sum(player_card) < 17:
                    willing = True

    while sum(opponent_card) < 17:
        generate_card(opponent_card)

    declare(player_card, opponent_card)


play = input(
    "Do you want to play a game of Blackjack ? Type 'y' or 'n' : ").lower()

if play == 'y':
    blackJack()

else:
    print("Goodbye")
