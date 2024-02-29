import os
import art

print(art.logo)
print("Welcome to the secret auction program.")

auction = []
game_over = False

while not game_over:
    person = {}
    name = input("What is your name : ")
    bid = int(input("What's your bid : $"))
    person["name"] = name
    person["bid"] = bid
    game_continue = input(
        "Are there any other bidder? Type 'yes' or 'no'. ").lower()
    auction.append(person)
    if game_continue == "no":
        game_over = True
    os.system('cls')

max = 0
bidperson = None

for bidder in auction:
    if bidder["bid"] > max:
        max = bidder["bid"]
        bidperson = bidder["name"]

print(f"The winner is {bidperson} with a bid of ${max}")
