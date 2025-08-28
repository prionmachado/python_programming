import random

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
} 

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
} 

def check_winning(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]  
        for column in columns:
            symbol_to_check = column[line]
            if symbol_to_check != symbol:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1) 
    
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol) 
 
    if len(all_symbols) < rows * cols:
        raise ValueError("Not enough symbols to fill the slot machine.")
    
    columns = [] 
    for _ in range(cols):
        column = [] 
        current_symbols = all_symbols[:] 
        for _ in range(rows): 
            value = random.choice(current_symbols)  
            current_symbols.remove(value) 
            column.append(value)

        columns.append(column)  
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print() 

def deposit():
    while True:
        try:
            amount = int(input("Enter the amount to deposit: "))
            if amount <= 0:
                print("Please enter a positive amount.")
            else:
                return amount
        except ValueError:
            print("Please enter a valid number.")  

def get_number_of_lines():
    while True:
        try:
            lines = int(input("Enter the number of lines to bet on (1-3): "))
            if 1 <= lines <= 3:
                return lines
            else:
                print("Please enter a number between 1 and 3.")
        except ValueError:
            print("Please enter a valid number.") 

def get_bet():
    while True:
        try:
            bet = int(input("Enter your bet amount on each line: "))
            if 1 <= bet <= 10000:
                return bet
            else:
                print("Amount must be between $1-10,000.") 
        except ValueError:
            print("Please enter a valid number.") 

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet() 
        total_bet = bet * lines

        if total_bet > balance:
            print("You do not have enough balance for this bet.") 
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet}.") 

    slot = get_slot_machine_spin(ROWS, COLS, symbol_count) 
    print_slot_machine(slot) 
    winnings, winning_lines = check_winning(slot, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines: {', '.join(map(str, winning_lines))}" if winning_lines else "You didn't win on any lines.")
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance: ${balance}")
        answer = input("Press Enter to play (or type 'q' to quit): ")
        if answer.lower() == 'q':
            print("Thanks for playing!")
            break
        balance += spin(balance) 
        if balance <= 0:
            print("You have run out of balance. Game over!")
            break

    print(f"Final balance: ${balance}")

if __name__ == "__main__":
    main() 