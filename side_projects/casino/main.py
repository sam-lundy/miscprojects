import random
from casino_art import logo

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "🎰": 2,
    "🍹": 4,
    "🍒": 6,
    "💩": 8
}

symbol_value = {
    "🎰": 10,
    "🍹": 7,
    "🍒": 4,
    "💩": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:   #IF YOU PUT ELSE AND THE FOR LOOP DOESN'T BREAK IT WILL RUN!!!
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    #This gets keys and values easily
    for symbol, symbol_count in symbols.items():    #This loops through symbol_count and gets key and value eg: symbol: A, symbol_count: 2
        #The _ is an anonymous variable used to not leave an unused variable like i
        for _ in range(symbol_count):   #This loops through the symbol_count (value) of A, 2 and adds A (2) times
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] #Copies a list by slicing beginning to end
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):    #enumerate gives you the index as you loop as well as the item
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()     #This extra print at the end makes each column print on a new line


def deposit():
    while True:
        amount = input("Please make a deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You cannot bet more than your current balance: ${balance}")

        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    if winnings > 0:
        print(f"You won ${winnings}.")       # *winning_lines is a splat/unpack operator, passes everything from winning_lines
        print(f"You won on line(s): ", *winning_lines)
    else:
        print("You didn't win this time. Please play again.")
    return winnings - total_bet

def main():
    print(logo)
    print("Welcome to the Lundy Casino!!~~ where your dreams become reality..")
    print(f"Please note the Max bet here is $100 and the minimum is $1.\n")
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        user_choice = input("Press enter to play. (q to quit).")
        if user_choice == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


main()