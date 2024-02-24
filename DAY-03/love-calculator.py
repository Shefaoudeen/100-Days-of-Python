print("The Love  Calculator is calculating your score...")

name1 = input().lower()
name2 = input().lower()

true = 0
true += name1.count("t") + name2.count("t")
true += name1.count("r") + name2.count("r")
true += name1.count("u") + name2.count("u")
true += name1.count("e") + name2.count("e")

love = 0
love += name1.count("l") + name2.count("l")
love += name1.count("o") + name2.count("o")
love += name1.count("v") + name2.count("v")
love += name1.count("e") + name2.count("e")

total = str(true)+str(love)

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos...")
elif total >= 40 and total <= 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}")
