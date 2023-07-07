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


symbols = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def symbol_printing():
    for symbol, name in symbols.items():
        print(symbol, end=' ')


def __main__():
    num1 = input("Enter the first number: ")
    if num1.isdigit():
        num1 = float(num1)
    else:
        print("Please enter a valid number.")

    should_continue = True

    while should_continue:

        while True:
            symbol_printing()
            oper = input("\nPick an operation: ")
            
            if oper not in symbols:
                print("Please enter a valid operator: \n")
                symbol_printing()
                break

            num2 = input("Enter the second number: ")
            if num2.isdigit():
                num2 = float(num2)
            else:
                print("Please enter a valid number: ")
                break

            calculation_func = symbols[oper]
            answer = calculation_func(num1, num2)
            print(f"{num1} {oper} {num2} = {answer}")
            keep_going = input("Would you like to perform another calculation with this result? (type y or n): ").lower()
            if keep_going == "n":
                terminate = input("Start a new calculation? (y or q to quit): ").lower()
                if terminate == "q":
                    should_continue = False
                    sys.exit()
                elif terminate == "y":
                    __init__()
            elif keep_going == "y":
                num1 = answer


def __init__():
    print(logo)
    __main__()

__init__()