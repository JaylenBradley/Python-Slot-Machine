import random 

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbolCount = {
    "A": 2, 
    "B": 4,
    "C": 6,
    "D": 8,
}

symbolVals = {
    "A": 5, 
    "B": 4,
    "C": 3,
    "D": 2,
}

def checkWinnings(columns, lines, bet, vals):
    winnings = 0
    winningLines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbolToCheck = column[line]
            if symbol != symbolToCheck:
                break
        else: #for/else statement; if break occurs, the else block is not executed
            winnings += vals[symbol] * bet
            winningLines.append(line + 1)
    
    return winnings, winningLines

def getSlotSpin(rows, cols, symbols):
    allSymbols = []
    for symbol, symbolCount in symbols.items(): #Gives the key value pair for each symbol in the dictionary
        for symbol in range(symbolCount): #'_' can be used to indicate a placeholder variable that will be replaced with a value: When you want to iterate but don't care about iteration value
            allSymbols.append(symbol)
    
    columns = []
    for i in range(cols):
        column = []
        currSymbols = allSymbols[:] #have to add ":" to create a copy of the list, not a reference
        for i in range(rows):
            value = random.choice(currSymbols)
            currSymbols.remove(value)
            column.append(value)        
        
        columns.append(column)
    return columns

def printSlots(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ") #end='' means that the print function will not add a newline character at the end of the line
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a valid amount")
    return amount

def getNumOfLines():
    while True:
        lines = input(f"Enter the number of lines you'd like to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"# of lines must be between 1 and {MAX_LINES}")
        else:
            print("Please enter a valid # of lines")
    return lines

def getBet():
    while True:
        bet = input(f"What would you like to bet on each line? (${MIN_BET} - {MAX_BET}): $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Bet must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a valid betting amount")
    return bet

def spin(bal):
    lines = getNumOfLines()
    
    while True:
        bet = getBet()
        totalBet = lines * bet

        if totalBet > bal:
            print(f"Insufficient funds to bet that amount. You only have ${bal}")
        else:
            break
    
    print(f"You're betting ${bet} on {lines} lines. Your total bet is ${totalBet}")
    
    
    slots = getSlotSpin(ROWS, COLS, symbolCount)
    printSlots(slots)
    winnings, winningLines = checkWinnings(slots, lines, bet, symbolVals)
    
    if winnings > 0:
        print(f"You won ${winnings}!")
        print(f"You won on lines", *winningLines) # '*' splat operator unpacks the list into individual arguments (displays all values in list)
    else:
        print("You didn't win anything :(")
    
    return winnings - totalBet

def main():
    bal = deposit()
    while True:
        print(f"Your current balance is ${bal}")
        answer = input("Press 'Enter' to spin the slots! ('Q' to quit): ").lower()
        if answer == "q":
            break
        bal += spin(bal)

        if bal <= 0:
            print("You're out of money! It's time to go home!")
            break
    
    print(f"Thanks for playing! Your final balance is ${bal}")

main()