print("Welcome to the Tic Tac Toe game (Two-Player Version)")
print("This game is for two players – no computer involved!")
print("We recommend making the output screen bigger for better visibility")
print("-------------------------------------------------------------")
print("-------------------------------------------------------------")
# Create the board positions (numbers 1-9) and a 3x3 game board
Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
gameBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = 3
columns = 3
# We now define the same functions that were previously used in the preliminary version as it seems that when imported they pollute the file with the CPU making random choices
def printboard():
    """
    Function to print the current state of the game board.
    """
    for x in range(rows):
        print("\n______________")
        print(" |", end="")
        for y in range(columns):
            print("", gameBoard[x][y], end=" |")
    print("\n______________")
# We also define again the function for the modification of the game board
def modgameboard(num, turn):
    """
    Modifies the game board at the position corresponding to 'num'
    with the player's symbol 'turn'.
    """
    num -= 1  # Adjust for 0-based indexing
    if num == 0:
        gameBoard[0][0] = turn
    elif num == 1:
        gameBoard[0][1] = turn
    elif num == 2:
        gameBoard[0][2] = turn
    elif num == 3:
        gameBoard[1][0] = turn
    elif num == 4:
        gameBoard[1][1] = turn
    elif num == 5:
        gameBoard[1][2] = turn
    elif num == 6:
        gameBoard[2][0] = turn
    elif num == 7:
        gameBoard[2][1] = turn
    elif num == 8:
        gameBoard[2][2] = turn
# We add the functions that will determine of which player is the turn and whether if the game continues or has ended
endloop = False
Count_Turns = 0
# We redefine the checkwin function, but now for a Player 1 and Player 2, no Python CPU involved
def checkwin(gameBoard):
    """
    Checks all winning combinations on the board.
    If a win is detected, prints the winner and sets endloop to True.
    """
    global endloop
    # Check rows for a win
    if gameBoard[0][0] == gameBoard[0][1] == gameBoard[0][2]:
        if gameBoard[0][0] == 'X':
            print("Player 1 wins!")
        elif gameBoard[0][0] == 'O':
            print("Player 2 wins!")
        endloop = True
        printboard()
    elif gameBoard[1][0] == gameBoard[1][1] == gameBoard[1][2]:
        if gameBoard[1][0] == 'X':
            print("Player 1 wins!")
        elif gameBoard[1][0] == 'O':
            print("Player 2 wins!")
        endloop = True
        printboard()
    elif gameBoard[2][0] == gameBoard[2][1] == gameBoard[2][2]:
        if gameBoard[2][0] == 'X':
            print("Player 1 wins!")
        elif gameBoard[2][0] == 'O':
            print("Player 2 wins!")
        endloop = True
        printboard()
    # Check columns for a win
    elif gameBoard[0][0] == gameBoard[1][0] == gameBoard[2][0]:
        if gameBoard[0][0] == 'X':
            print("Player 1 wins!")
        elif gameBoard[0][0] == 'O':
            print("Player 2 wins!")
        endloop = True
        printboard()
    elif gameBoard[0][1] == gameBoard[1][1] == gameBoard[2][1]:
        if gameBoard[0][1] == 'X':
            print("Player 1 wins!")
        elif gameBoard[0][1] == 'O':
            print("Player 2 wins!")
        endloop = True
        printboard()
    elif gameBoard[0][2] == gameBoard[1][2] == gameBoard[2][2]:
        if gameBoard[0][2] == 'X':
            print("Player 1 wins!")
        elif gameBoard[0][2] == 'O':
            print("Player 2 wins!")
        endloop = True
        printboard()
    # Check diagonals for a win
    elif gameBoard[0][0] == gameBoard[1][1] == gameBoard[2][2]:
        if gameBoard[0][0] == 'X':
            print("Player 1 wins!")
        elif gameBoard[0][0] == 'O':
            print("Player 2 wins!")
        endloop = True
        printboard()
    elif gameBoard[2][0] == gameBoard[1][1] == gameBoard[0][2]:
        if gameBoard[2][0] == 'X':
            print("Player 1 wins!")
        elif gameBoard[2][0] == 'O':
            print("Player 2 wins!")
        endloop = True
        printboard()
# Now from the previous
while not endloop and Count_Turns < 9:
    printboard()
    # Alternate turns: even turns for Player 1 ('X'), odd turns for Player 2 ('O')
    if Count_Turns % 2 == 0:
        try:
            picknumber = int(input("\nPlayer 1 (X), choose a number from 1 to 9: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        symbol = 'X'
    else:
        try:
            picknumber = int(input("\nPlayer 2 (O), choose a number from 1 to 9: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        symbol = 'O'

    if picknumber not in Numbers:
        print("That slot has already been taken or is invalid, please choose another one.")
        continue
    elif 1 <= picknumber <= 9:
        modgameboard(picknumber, symbol)
        Numbers.remove(picknumber)
        checkwin(gameBoard)
        Count_Turns += 1
    else:
        print("Invalid input, please choose an integer between 1 and 9.")

if not endloop:
    print("It's a tie!")
    printboard()