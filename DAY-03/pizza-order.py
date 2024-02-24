print("Thank you for choosing Python Pizza Deliveries!")

size = input()
add_pepperoni = input()
extra_cheese = input()

bill = 0

if size == "S":
    if add_pepperoni == "Y":
        bill += 2
    bill += 15
else:
    if add_pepperoni == "Y":
        bill += 3
    if size == "M":
        bill += 20
    else:
        bill += 25

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")
