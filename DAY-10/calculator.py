import art
import os


def add(n1, n2):
    """Returns sum of two nums"""
    return n1+n2


def sub(n1, n2):
    """Returns difference of two nums"""
    return n1-n2


def mul(n1, n2):
    """Returns product of two nums"""
    return n1*n2


def div(n1, n2):
    """Returns division of two nums"""
    return round(n1/n2, 2)


def calculator():
    """Perform normal calculation"""
    print(art.logo)

    answer = None
    continue_calculation = True
    num1 = float(input("What is the first number ? "))

    while continue_calculation:
        operand = input("Select any operation(+,-,/,*) : ")
        num2 = float(input("What is the second number ?"))
        operation_function = {
            '+': add,
            '-': sub,
            '*': mul,
            '/': div,
        }
        operation = operation_function[operand]
        answer = operation(num1, num2)
        print(f"{num1} {operand} {num2} = {answer}")

        next_operation = input(
            f"Type 'y' to continue calculationg with {answer}, or type 'n' to start a new caluation: ").lower()
        if next_operation == 'n':
            os.system('cls')
            calculator()
        num1 = answer


calculator()
