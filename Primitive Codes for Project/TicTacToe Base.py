#Import a random choice from the Python CPU
import random

print("Welcome to the Tic Tac Toe game"
      "\nThis game will serve as base for the football inspired multiplayer versions")
print("In this game, a single player will play against the computer")
print("We reccomend to make the ouput screen bigger for better visibility")
print("-------------------------------------------------------------")
print("-------------------------------------------------------------")
#Now we create the possible numbers in the board, assigned to each of the positions
Numbers = [1,2,3,4,5,6,7,8,9]
gameBoard = [[1,2,3], [4,5,6], [7,8,9]]
# Now we define the number of rows and columns in the game
rows = 3
columns = 3
# Now a function is defined in order to print the game board
def printboard():
    """
    Function that will print the Tic Tac Toe game board
    :return: A matrix with the game board and the
    coordinates of the array, in different lines
    """
    for x in range(rows):
        print("\n______________")
        print(" |", end="")
        for y in range(columns):
            print("", gameBoard[x][y], end=" |")
    # With this next print function with the \n command
    # We can print the string in the next line
    print("\n______________")

def modgameboard(num, turn):
    """
    Function that will modify the game board accordingly to the number
    introduced and the turn that is playing at the moment
    :param num: Num will be an integer between 1 and 9, that will
    be the number corresponding to a certain position in the game board
    :param turn: Turn will identify the player that is introducing the
    integer assigning 'X' or 'O' to the corresponding position
    :return: The updated version of the game board after the input
    received by either player.
    """
    num -=1
    #The assignment of numbers corresponds to a certain coordinate in the
    #matrix of the game board [0][0] will be top left, with the first
    #number being the rows and the second number being the columns
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

# We define this variable in advance,
# which is going to be to end the game
endloop = False
#This variable here will keep track of the number of turns and
#assing the turn to the corresponding player
Count_Turns = 0

def checkwin(gameBoard):
    #This line of code is vital as it will retrieve the function endloop
    # from the global environment so then we can use it here to check
    # If anyone has won
    global endloop
    """
    Checks for the x-axis and y-axis of the Matrix, if there is a sequence
    of "X,X,X" or "O,O,O" in a straight line, then the player wins
    :param gameBoard: The Matrix used for the game board
    :return: The player that has won the Tic Tac Toe game
    """
    # X-axis wins: We use the different coordinates of the matrix to
    # address the possibility of a win, using the variable endloop, to
    # finish the game and print the name of the player that wins, we
    # have to address each possibility and coordinate to each player
    if gameBoard[0][0] == gameBoard[0][1] == gameBoard[0][2] == 'X':
        print("Player wins!")
        endloop = True
    elif gameBoard[1][0] == gameBoard[1][1] == gameBoard[1][2] == 'X':
        print("Player wins!")
        endloop = True
    elif gameBoard[2][0] == gameBoard[2][1] == gameBoard[2][2] == 'X':
        print("Player wins!")
        endloop = True
    #Adress Possibility of Python Winning the game:
    elif gameBoard[0][0] == gameBoard[0][1] == gameBoard[0][2] == 'O':
        print("Python wins!")
        endloop = True
    elif gameBoard[1][0] == gameBoard[1][1] == gameBoard[1][2] == 'O':
        print("Python wins!")
        endloop = True
    elif gameBoard[2][0] == gameBoard[2][1] == gameBoard[2][2] == 'O':
        print("Python wins!")
        endloop = True
    # Y-axis wins: Address the possibilities for wins
    # across the Y-axis of the matrix, both for 'X' and 'O'
    if gameBoard[0][0] == gameBoard[1][0] == gameBoard[2][0] == 'X':
        print("Player wins!")
        endloop = True
    elif gameBoard[0][0] == gameBoard[1][0] == gameBoard[2][0] == 'O':
        print("Python wins!")
        endloop = True
    elif gameBoard[0][1] == gameBoard[1][1] == gameBoard[2][1] == 'X':
        print("Player wins!")
        endloop = True
    elif gameBoard[0][1] == gameBoard[1][1] == gameBoard[2][1] == 'O':
        print("Python wins!")
        endloop = True
    elif gameBoard[0][2] == gameBoard[1][2] == gameBoard[2][2] == 'X':
        print("Player wins!")
        endloop = True
    elif gameBoard[0][2] == gameBoard[1][2] == gameBoard[2][2] == 'O':
        print("Python wins!")
        endloop = True
    # Cross-axis wins: There are two ways to win crossing the axis, one
    # from top-left to bottom right and another one from top right to
    # bottom left
    # For top right to bottom left
    if gameBoard[0][0] == gameBoard[1][1] == gameBoard[2][2] == 'X':
        print("Player wins!")
        endloop = True
    elif gameBoard[0][0] == gameBoard[1][1] == gameBoard[2][2] == 'O':
        print("Python wins!")
        endloop = True
    elif gameBoard[2][0] == gameBoard[1][1] == gameBoard[0][2] == 'X':
        print("Player wins!")
        endloop = True
    elif gameBoard[2][0] == gameBoard[1][1] == gameBoard[0][2] == 'O':
        print("Python wins!")
        endloop = True

# Now we have to address each one of the turns after the checkwin function so we check for a win in each turn
# and also develop the logic behind every turn
while endloop == False:
    #It's 'X' turn if we take the turn divided by two and remainder is equal to 1
    if Count_Turns % 2 == 1:
        printboard()
        # \n again to get a new line, and int to transform input
        picknumber = int(input("\n Choose a number from 1 to 9: "))
        # Now validate the input
        if picknumber >= 1 or picknumber <= 9:
            modgameboard(picknumber, 'X')
            #remove the number picked in turn from possibilities:
            Numbers.remove(picknumber)
            checkwin(gameBoard) # checks if someone has won the game
        else:
            #If the input is invalid print the following
            print("Invalid input, please introduce an integer between 1 and 9")
        Count_Turns = Count_Turns + 1
    else:
        #Adress the 'O' turns, or the turns by the Python CPU
        while True:
            #CPU will pick from the list provided by numbers
            ChoicePython = random.choice(Numbers)
            print("\n CPU chose:", ChoicePython)
            #If the CPU made a valid choice, then introduce their choice
            if ChoicePython in Numbers:
                modgameboard(ChoicePython, 'O')
                #Remove the number from the list of Possible Numbers
                Numbers.remove(ChoicePython)
                checkwin(gameBoard)
                Count_Turns = Count_Turns + 1
                # Now that we have the logic to operate the game
                # we can break out of the loop, as it is while loop
                break
# Now we have all the code necessary for the Tic Tac Toe game against Python

