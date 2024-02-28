def prime_checker(number):
    if number == 1:
        print("Not a Prime Number")

    i = 2
    while i < number:
        if number % i == 0:
            print("Not a Prime Number")
            break
        i += 1

    if i == number:
        print("Prime Number")


n = int(input())
prime_checker(number=n)
