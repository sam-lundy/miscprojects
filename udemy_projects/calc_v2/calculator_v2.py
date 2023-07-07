from calc_art import logo
import sys

def add(n1, n2):
    return n1 + n2
    
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def exponent(n1, n2):
    return n1 ** n2

def remainder(n1, n2):
    return n1 % n2

symbols = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": exponent,
    "%": remainder
}


def symbol_printing():
    for symbol, name in symbols.items():
        print(symbol, end=' ')


def calc():
    print(logo)
    num1 = float(input("Enter the first number: "))
    print()

    while True:
        try:
            symbol_printing()
            print("\n")
            oper = input("Pick an operation: \n")
            
            if oper in symbols:
                break
            else:
                print("Not an accepted operator.\n")

        except KeyError:
            print("Invalid Input")

#Entering a non number made program crash, add another try/except block?
    while True:
        num2 = float(input("Enter the second number: "))

        if oper == "/" and num2 == 0:
            print("You can't divide by zero!!")
            calc()

        calculation_func = symbols[oper]
        answer = calculation_func(num1, num2)
        print(f"{num1} {oper} {num2} = {answer}")

        keep_going = input("Would you like to perform another calculation with this result? (type y or n): ").lower()
        if keep_going == "n":
            terminate = input("Start a new calculation? (y or q to quit): ").lower()
            if terminate == "q":
                sys.exit()
            elif terminate == "y":
                calc()
        elif keep_going == "y":
            num1 = answer


calc()