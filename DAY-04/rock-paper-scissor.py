import asciiArt
import random

choice = int(
    input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

art = [asciiArt.rock, asciiArt.paper, asciiArt.scissors]

computer_choice = random.randint(0, 2)

print("Your choice : ")
print(art[choice])

print("\nComputer chose: ")
print(art[computer_choice])

if choice == 0:
    if computer_choice == 0:
        print("Match Draw")
    elif computer_choice == 1:
        print("You lose")
    elif computer_choice == 2:
        print("You win")

elif choice == 1:
    if computer_choice == 1:
        print("Match Draw")
    elif computer_choice == 2:
        print("You lose")
    elif computer_choice == 0:
        print("You win")

elif choice == 2:
    if computer_choice == 2:
        print("Match Draw")
    elif computer_choice == 0:
        print("You lose")
    elif computer_choice == 1:
        print("You win")
