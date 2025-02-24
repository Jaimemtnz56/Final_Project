# We do not need to change this two functions for the current model for 2 players
from Preliminarycodes.TicTacToe_Base import printboard as printboard_v2
from Preliminarycodes.TicTacToe_Base import modgameboard as modgameboard_v2

#Print the game board and introduction as on the preliminary version
print("Welcome to the Tic Tac Toe multiplayer game!!"
      "\nThis game will serve as base for the football inspired versions.")
print("In this game, we will need to players to take turns.")
print("We recommend to make the output screen bigger for better visibility!")
print("-------------------------------------------------------------")
print("-------------------------------------------------------------")
#Now we create the possible numbers in the board, assigned to each of the positions
Numbers = [1,2,3,4,5,6,7,8,9]
gameBoard = [[1,2,3], [4,5,6], [7,8,9]]
# Now we define the number of rows and columns in the game
rows = 3
columns = 3
# We add all the code that holds outside of defining functions on the single player version
endloopv2 = False
Count_Turnsv2 = 0
#Both these objects are vital to our game as they will determine who is the player in turn and whether
#the game must keep going or not, based on who has won the game, ending the loop

# Now we must change the checkwin function, in order to refer to Player 1 'O' and 2 'X'

def checkwinv2(gameBoard):
    #This line of code is vital as it will retrieve the function endloop
    # from the global environment so then we can use it here to check
    # If anyone has won, this line was found by research online
    global endloopv2
    """
    Checks for every possible straight line combination of three 'X' or 'O'
    through the x-axis, y-axis or both. If the function finds it will end the game and 
    determine the winner.
    :param gameBoard: The Matrix used for the game board
    :return: The player that has won the Tic Tac Toe game (Player 1 or Player 2)
    """
    # X-axis wins: We use the different coordinates of the matrix to
    # address the possibility of a win, using the variable endloop, to
    # finish the game and print the name of the player that wins, we
    # have to address each possibility and coordinate to each player
    # being Player 1 the 'O' and Player 2 the 'X'
    if gameBoard[0][0] == gameBoard[0][1] == gameBoard[0][2] == 'X':
        print("Player 1 wins!")
        endloopv2 = True
        printboard_v2()
    elif gameBoard[1][0] == gameBoard[1][1] == gameBoard[1][2] == 'X':
        print("Player 1 wins!")
        endloopv2 = True
        printboard_v2()
    elif gameBoard[2][0] == gameBoard[2][1] == gameBoard[2][2] == 'X':
        print("Player 1 wins!")
        endloopv2 = True
        printboard_v2()
    #Adress Possibility of Python Winning the game:
    elif gameBoard[0][0] == gameBoard[0][1] == gameBoard[0][2] == 'O':
        print("Player 2 wins!")
        endloopv2 = True
        printboard_v2()
    elif gameBoard[1][0] == gameBoard[1][1] == gameBoard[1][2] == 'O':
        print("Player 2 wins!")
        endloopv2 = True
        printboard_v2()
    elif gameBoard[2][0] == gameBoard[2][1] == gameBoard[2][2] == 'O':
        print("Player 2 wins!")
        endloopv2= True
        printboard_v2()
    # Y-axis wins: Address the possibilities for wins
    # across the Y-axis of the matrix, both for 'X' and 'O'
    if gameBoard[0][0] == gameBoard[1][0] == gameBoard[2][0] == 'X':
        print("Player 1 wins!")
        endloopv2 = True
        printboard_v2()
    elif gameBoard[0][0] == gameBoard[1][0] == gameBoard[2][0] == 'O':
        print("Player 2 wins!")
        endloopv2 = True
        printboard_v2()
    elif gameBoard[0][1] == gameBoard[1][1] == gameBoard[2][1] == 'X':
        print("Player 1 wins!")
        endloopv2 = True
        printboard_v2()
    elif gameBoard[0][1] == gameBoard[1][1] == gameBoard[2][1] == 'O':
        print("Player 2 wins!")
        endloopv2 = True
        printboard_v2()
    elif gameBoard[0][2] == gameBoard[1][2] == gameBoard[2][2] == 'X':
        print("Player 1 wins!")
        endloopv2 = True
        printboard_v2()
    elif gameBoard[0][2] == gameBoard[1][2] == gameBoard[2][2] == 'O':
        print("Player 2 wins!")
        endloopv2 = True
        printboard_v2()
    # Cross-axis wins: There are two ways to win crossing the axis, one
    # from top-left to bottom right and another one from top right to
    # bottom left
    # For top right to bottom left
    if gameBoard[0][0] == gameBoard[1][1] == gameBoard[2][2] == 'X':
        print("Player 1 wins!")
        endloopv2 = True
        printboard_v2()
    elif gameBoard[0][0] == gameBoard[1][1] == gameBoard[2][2] == 'O':
        print("Player 2 wins!")
        endloopv2 = True
        printboard_v2()
    elif gameBoard[2][0] == gameBoard[1][1] == gameBoard[0][2] == 'X':
        print("Player 1 wins!")
        endloopv2 = True
        printboard_v2()
    elif gameBoard[2][0] == gameBoard[1][1] == gameBoard[0][2] == 'O':
        print("Player 2 wins!")
        endloopv2 = True
        printboard_v2()

# Now we have to address each one of the turns after the checkwin function so we check for a win in each turn
# and also develop the logic behind every turn, both for Player 1 and Player 2
while endloopv2 == False:
    #It's 'X' turn if we take the turn divided by two and remainder is equal to 1
    # We are first adressing the turns by Player 2, or 'X'
    if Count_Turnsv2 % 2 == 1:
        printboard_v2()
        # \n again to get a new line, and int to transform input
        picknumber = int(input("\n Player 1, Choose a number from 1 to 9: "))
        # Now validate the input
        if picknumber >= 1 or picknumber <= 9:
            modgameboard_v2(picknumber, 'X')
            #remove the number picked in turn from possibilities:
            Numbers.remove(picknumber)
            checkwinv2(gameBoard) # checks if someone has won the game
        else:
            #If the input is invalid print the following
            print("Invalid input, please introduce an integer between 1 and 9")
        Count_Turnsv2 = Count_Turnsv2 + 1
    else:
        #Adress the 'O' turns, or the turns by the Player 1
        while True:
            if Count_Turnsv2 % 2 == 0:
                printboard_v2()
                # \n again to get a new line, and int to transform into input
                picknumber2 = int(input("\n Player 2, choose a number from 1 to 9: "))
                # We validate the input by Player 2
                if picknumber2 >= 1 or picknumber2 <= 9:
                    modgameboard_v2(picknumber2, 'O')
                    #remove the picked number in turn from possibilities:
                    Numbers.remove(picknumber2)
                    checkwinv2(gameBoard)
                else:
                    # If the input is invalid print the following
                    print("Invalid input, please introduce an integer between 1 and 9")
                #Add one turn
                Count_Turnsv2 = Count_Turnsv2 + 1
                break




