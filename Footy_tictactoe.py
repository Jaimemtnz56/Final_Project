def Footy_tictactoe():
    """
    This function will play a game of Tic-Tac-Toe based on football. The idea of the game is the same as a normal
    Tic-Tac-Toe, but with a catch, for each cell, there are conditions that have to be satisfied with a football player.
    For further simplicity of the game, four categories have been added that can be used in the grid, they are the
    following: Country, Club, League, Ballon D'or Winner and Champions League winner. There are four sets to play the game,
    increasing in difficulty. From set one to four, the logic and programming behind the game is the same as used in
    the preliminary versions, just adding the use of dictionaries to assign players to their respective cells, through
    using the numbers. The maximum pool of players for each condition is 6, the most famous players will be included or
    the most influential for that specific category, the input might not be always wrong, just not included within the conditions,
    try and think about the basic answers, the most influential ones (e.g. for Liverpool and Spain Xabi Alonso, not Iago Aspas).
    Finally, it is important to note that special characters are not supported in player names, therefore the name must be
    introduced in the following way: "Firstname Lastname" or just "Lastname" making García an invalid name, Garcia would be valid.
    :return: The Footy Tic-Tac-Toe game. (Football inspired version of a Tic-Tac-Toe game)
    """
# DIFFERENT CONFIGURATIONS FOR THE TIC TAC TOE GAME
    def config_game1():
        """
        First configuration for the game, only including the conditions for countries and clubs. Maximum of 6 players
        are valid for each category, the most famous ones will be included, categories are ideated for having no more than
        5 options generally. It is important to note that the player will be included for the team he was most influential
        for in case of being available for multiple options, Nazario and Figo are considered Real Madrid players, not
        Barcelona players for this game and configurations.
        :return: The game board configuration with the following labels and the players that can be assigned to each cell.
        """
        # Configuration for Game 1
        row_labels = ["REAL MADRID", "BARÇA", "ATLETI"]
        col_labels = ["PORTUGAL", "HOLLAND", "BRAZIL"]
        player_to_cell = {
            "Cristiano Ronaldo": 1, "Cristiano": 1, "Luis Figo": 1, "Figo": 1, "Pepe": 1, "Ricardo Carvalho": 1,
            "Carvalho": 1, "Fabio Coentrao": 1, "Coentrao": 1,
            "Clarence Seedorf": 2, "Seedorf": 2, "Ruud van Nistelrooy": 2, "Van Nistelrooy": 2, "Arjen Robben": 2,
            "Robben": 2, "Wesley Sneijder": 2, "Sneijder": 2, "Rafael van der Vaart": 2, "Van der Vaart": 2,
            "Klaas-Jan Huntelaar": 2, "Huntelaar": 2,
            "Roberto Carlos": 3, "Ronaldo Nazario": 3, "Ronaldo": 3, "Kaka": 3, "Marcelo Vieira": 3, "Marcelo": 3,
            "Casemiro": 3, "Vinicius Junior": 3, "Vinicius": 3,
            "Deco": 4, "Baia": 4, "Simao Sabrosa": 4, "Andre Gomes": 4, "Nelson Semedo": 4, "Semedo": 4,
            "Johan Cruyff": 5, "Cruyff": 5, "Ronald Koeman": 5, "Koeman": 5, "Patrick Kluivert": 5, "Kluivert": 5,
            "Marc Overmars": 5, "Overmars": 5, "Frenkie de Jong": 5, "De Jong": 5, "Edgar Davids": 5, "Davids": 5,
            "Romario": 6, "Rivaldo": 6, "Ronaldinho Gaucho": 6, "Ronaldinho": 6, "Dani Alves": 6, "Alves": 6,
            "Raphinha": 6, "Vitor Roque": 6,
            "Jorge Alberto Mendonça": 7, "Mendonça": 7, "Paulo Futre": 7, "Futre": 7, "Hugo Leal": 7, "Leal": 7,
            "Pizzi": 7, "Diogo Jota": 7, "Jota": 7, "Gelson Martins": 7, "Martins": 7,
            "Jimmy Hasselbaink": 8, "Hasselbaink": 8, "John Heitinga": 8, "Heitinga": 8, "Kizito Musampa": 8,
            "Musampa": 8, "Memphis Depay": 8, "Depay": 8, "Merel van Dongen": 8, "Van Dongen": 8,
            "Sari van Veenedaal": 8, "Van Veenedaal": 8,
            "Diego Costa": 9, "Filipe Luis": 9, "João Miranda": 9, "Miranda": 9, "Matheus Cunha": 9, "Cunha": 9
        }
        return row_labels, col_labels, player_to_cell

    def config_game2():
        """
        Second configuration of the game now introducing the new conditions Ballon D'or Winner and Champions League winner,
        players that have done both are only counted for one category, in this case Zinedine Zidane is considered for Ballon D'or Winner
        as he has more than Benzema, as he is now considered as UCL winner for this game, the player will not lose the turn when introducing
        an invalid input.
        :return: The game board configuration and game configuration according to the conditions below.
        """
        # Configuration for Game 2
        row_labels = ["UCL WINNER", "DORTMUND", "BALLON D'OR"]
        col_labels = ["CZECHIA", "FRANCE", "ENGLAND"]
        player_to_cell = {
            "Milan Baros": 1, "Baros": 1, "Vladimir Smicer": 1, "Smicer": 1, "Marek Jankulovski": 1, "Jankulovski": 1, "Petr Cech": 1, "Cech": 1,
            "Karim Benzema": 2, "Benzema": 2, "Didier Deschamps": 2, "Deschamps": 2, "Bixente Lizarazu": 2, "Lizarazu": 2, "Christophe Dugarry": 2, "Dugarry": 2, "Kingsley Coman": 2, "Coman": 2,
            "Steven Gerrard": 3, "Gerrard": 3, "Frank Lampard": 3, "Lampard": 3, "Wayne Rooney": 3, "Rooney": 3, "Rio Ferdinand": 3, "Ferdinand": 3, "David Beckham": 3, "Beckham": 3, "Paul Scholes": 3, "Scholes": 3,
            "Jan Koller": 4, "Koller": 4, "Tomas Rosicky": 4, "Rosicky": 4, "Patrik Berger": 4, "Berger": 4,
            "Ousmane Dembele": 5, "Dembele": 5, "Axel Zagadou": 5, "Zagadou": 5, "Anthony Modeste": 5, "Modeste": 5, "Damien Le Tallec": 5, "Le Tallec": 5, "Soumaila Coulibaly": 5, "Coulibaly": 5,
            "Jadon Sancho": 6, "Sancho": 6, "Jude Bellingham": 6, "Bellingham": 6, "Jamie Bynoe Gittens": 6, "Bynoe Gittens": 6, "Carney Chukwuemeka": 6, "Chukwuemeka": 6,
            "Josef Masopust": 7, "Masopust": 7, "Pavel Nedved": 7, "Nedved": 7,
            "Raymond Kopa": 8, "Kopa": 8, "Michel Platini": 8, "Platini": 8, "Jean Pierre Papin": 8, "Papin": 8, "Zinedine Zidane": 8, "Zidane": 8,
            "Stanley Matthews": 9, "Matthews": 9, "Bobby Charlton": 9, "Charlton": 9, "Kevin Keegan": 9, "Keegan": 9, "Michael Owen": 9, "Owen": 9
         }
        return row_labels, col_labels, player_to_cell

    def config_game3():
        """
        Third configuration of the game, first mixing all the conditions freely, players that have done both are only counted for one category,
        In the case of Cristiano Ronaldo he is counted for the Ballon D'or only, not for Manchester UDT and Portugal.
        :return: The third variety of the game board with its respective inputs.
        """
        # Configuration for Game 3
        row_labels = ["MANCHESTER UDT", "LIVERPOOL", "BALLON D'OR"]
        col_labels = ["PORTUGAL", "MAN CITY", "BARÇA"]
        player_to_cell = {
            "Nani": 1, "Luis Nani": 1, "Bebe": 1, "Tiago Bebe": 1, "Joel Pereira": 1, "Pereira": 1, "Diogo Dalot": 1, "Dalot": 1,"Bruno Fernandes": 1, "Fernandes": 1,
            "Denis Law": 2, "Law": 2, "Brian Kidd": 2, "Kidd": 2, "Peter Schmeichel": 2, "Schmeichel": 2, "Andy Cole": 2, "Cole": 2, "Carlos Tevez": 2, "Tevez": 2, "Owen Hargreaves": 2, "Hargreaves": 2,
            "Mark Hughes": 3, "Hughes": 3, "Jordi Cruyff": 3, "Laurent Blanc": 3, "Blanc": 3, "Henrik Larsson": 3, "Larsson": 3, "Victor Valdes": 3, "Valdes": 3, "Zlatan Ibrahimovic": 3, "Ibrahimovic": 3, "Gerard Pique": 3, "Pique": 3,
            "Diogo Jota": 4, "Jota": 4, "Fabio Carvalho": 4, "Carvalho": 4, "Raul Meireles": 4, "Meireles": 4, "Joao Carlos Teixeira": 4, "Teixeira": 4,"Tiago Ilori": 4, "Ilori": 4, "Rafael Camacho": 4, "Camacho": 4,
            "James Milner": 5, "Milner": 5, "Raheem Sterling": 5, "Sterling": 5, "Robbie Fowler": 5, "Fowler": 5, "Steve McManaman": 5, "McManaman": 5, "Dietmar Hamann": 5, "Hamann": 5,"Craig Bellamy": 5, "Bellamy": 5,
            "Luis Suarez": 6, "Suarez": 6, "Javier Mascherano": 6, "Mascherano": 6, "Philippe Coutinho": 6, "Coutinho": 6, "Pepe Reina": 6, "Reina": 6, "Luis Garcia": 6, "Garcia": 6, "Boudewijn Zenden": 6, "Zenden": 6,
            "Eusebio": 7, "Eusebio da Silva Ferreira": 7, "Luis Figo": 7, "Figo": 7, "Cristiano Ronaldo": 7, "Cristiano": 7,
            "Rodrigo Hernandez": 8, "Rodri": 8,
            "Johan Cruyff": 9, "Cruyff": 9, "Hristo Stoichkov": 9, "Stoichkov": 9, "Rivaldo": 9, "Ronaldinho Gaucho": 9, "Ronaldinho": 9, "Lionel Messi": 9, "Messi": 9
        }
        return row_labels, col_labels, player_to_cell

    def config_game4():
        """
        Fourth configuration for the game, the difficulty lies on the scarcity of possible answers for each condition
        but either way the players available for those slots are well and widely known, for the Spanish row, I have decided
        to go for a mix between influence and the best players and most influential for those teams overall
        :return: The fourth variety of the game board with its respective inputs.
        """
        # Configuration for Game 4
        row_labels = ["UKRAINE", "SPAIN", "RUSSIA"]
        col_labels = ["BALLON D'OR", "REAL MADRID", "ARSENAL"]
        player_to_cell = {
            "Andriy Shevchenko": 1, "Shevchenko": 1,
            "Andriy Lunin": 2, "Lunin": 2, "Oleh Luzhnyi": 2, "Luzhnyi": 2,
            "Oleksandr Zinchenko": 3,
            "Luis Suarez": 4, "Suarez": 4, "Rodrigo Hernandez": 4, "Rodri": 4,
            "Sergio Ramos": 5, "Ramos": 5, "Iker Casillas": 5, "Casillas": 5, "Dani Carvajal": 5, "Carvajal": 5, "Xabi Alonso": 5, "Alonso": 5, "Lucas Vazquez": 5, "Vazquez":5, "Asier Illarramendi": 5, "Illarramendi": 5, "Nacho": 5, "Marco Asensio": 5, "Asensio": 5,
            "Cesc Fabregas": 6, "Santi Cazorla": 6, "Cazorla": 6, "Mikel Arteta": 6, "Arteta": 6, "Mikel Merino": 6, "Merino": 6, "Hector Bellerin": 6, "Bellerin": 6, "Cesar Azpilicueta": 6, "Azpilicueta": 6, "Nacho Monreal": 6, "Monreal": 6,
            "Lev Yashin": 7, "Yashin": 7,
            "Denis Cheryshev": 8, "Cheryshev": 8,
            "Andrei Arshavin": 9, "Arshavin": 9,
          }
        return row_labels, col_labels, player_to_cell

# SETTING UP THE GAME
    def play_game(Team_1, Team_2, row_labels, col_labels, player_to_cell):
        """
        Allows for the game to actually be played. It sets up the game board and the values inside each cell, that
        will later be changed with another function.
        :param Team_1: Home team, the team that will be assigned the symbol "X" on the board.
        :param Team_2: Away team, the team that will be assigned the symbol "O" on the board.
        :param row_labels: According to the different configurations of the game, the labels with the row conditions for the game
        :param col_labels: According to the different configurations of the game, the labels with the column conditions for the game
        :param player_to_cell: The dictionary that allows for that specific configuration to be used and have the players assigned
        to a certain cell on the board, allowing for the game to be played
        :return: The logic of the game board and the possible inputs for each category and respective cell.
        """
        # Basic game setup
        gameBoard = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
        rows = 3
        columns = 3
        available_positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        home_team = "X"
        away_team = "O"
        endloop = False
        Count_Turns = 0

# PRINT THE GAME BOARD
        def printboard():
            """
            Function that prints the game board, allowing for the visual representation of every step of the game, it
            prints the board after every turn with its updated version. The labels are also printed for every cell and category
            :return: Prints the game board with its respective labels and cells at any given moment during the game, the current
            state of the game board at that moment during the game .
            """
            print(" " * 20, end="")
            for header in col_labels:
                print(f"{header:^15}", end=" ")
            print("\n" + "-" * 70)
            for i in range(rows):
                print(f"{row_labels[i]:<15}", end="|")
                for j in range(columns):
                    print(f"{str(gameBoard[i][j]):^15}", end="|")
                print("\n" + "-" * 70)

# CREATE A FUNCTION THAT MODIFIES THE CURRENT STATE OF THE GAME BOARD
        def modgameboard(num, symbol):
            """
            Allows for the game board to be modified after each input, adjusting for the 0 based indexing that python uses
            for lists and arrays. It will substitute the cell with its current value with the symbol that made the move and
            introduced a valid input for one of the categories.
            :param num: Number in the array (from 1 to 9) that will be modified according to the player to cell dictionary.
            :param symbol: 'X' or 'O' depending on the team that made the move and introduced a valid input for one of the category.
            :return: The updated game board with the modified cell after each move, but it does not print the current state of the board
            after it has been modified by this function.
            """
            nonlocal gameBoard # Imports the Game board into this specific function
            num -= 1  # Adjust for 0-based indexing
            if num == 0:
                gameBoard[0][0] = symbol
            elif num == 1:
                gameBoard[0][1] = symbol
            elif num == 2:
                gameBoard[0][2] = symbol
            elif num == 3:
                gameBoard[1][0] = symbol
            elif num == 4:
                gameBoard[1][1] = symbol
            elif num == 5:
                gameBoard[1][2] = symbol
            elif num == 6:
                gameBoard[2][0] = symbol
            elif num == 7:
                gameBoard[2][1] = symbol
            elif num == 8:
                gameBoard[2][2] = symbol

# CREATE A FUNCTION THAT PRINTS THE RESULT OF THE GAME
        def declare_winner(symbol):
            """
            This function declares the winner of the game, it severs a complementary purpose to the checkwin function.
            :param symbol: 'X' or 'O' depending on the team that won the game.
            :return: A f string with the team that has won the game of tic-tac-toe
            """
            nonlocal endloop # Imports endloop into this specific function
            if symbol == home_team:
                print(f"Incredible! {Team_1} has scored a game winning goal!")
                print(f"{Team_1} has won the championship with an incredible performance!")
            elif symbol == away_team:
                print(f"Incredible! {Team_2} has scored a game winning goal!")
                print(f"{Team_2} has won the championship with an incredible performance!")
            endloop = True
            printboard()

# CREATE A COMPLEMENTARY FUNCTION TO THE PREVIOUS ONE THAT RUNS THE WHOLE LOGIC OF WHO HAS WON
        def checkwin(board):
            """
            Creates the logic behind checking the winner of the game, this functions analyzes the current state of the
            game board and determines if there is a winner and who it is or if the game is a tie. It checks for that condition
            by comparing the cells to each other and seeing the symbol that they have assigned, if there are three of the same
            symbol in a straight line, it declares the winner. This is a simplified version of the function from the preliminary
            versions, as it now checks for the content of the cells and lets other function handle the result of the game, it does
            not check for every single possibility that there is for both players to determine the winner
            :param board: The current state of the tic-tac-toe game board.
            :return: The result of the game, but it does not print the team that won or if there was a tie
            """
            nonlocal endloop # Imports endloop into the function
            # Check rows
            if board[0][0] == board[0][1] == board[0][2]:
                declare_winner(board[0][0])
            elif board[1][0] == board[1][1] == board[1][2]:
                declare_winner(board[1][0])
            elif board[2][0] == board[2][1] == board[2][2]:
                declare_winner(board[2][0])
            # Check columns
            elif board[0][0] == board[1][0] == board[2][0]:
                declare_winner(board[0][0])
            elif board[0][1] == board[1][1] == board[2][1]:
                declare_winner(board[0][1])
            elif board[0][2] == board[1][2] == board[2][2]:
                declare_winner(board[0][2])
            # Check diagonals
            elif board[0][0] == board[1][1] == board[2][2]:
                declare_winner(board[0][0])
            elif board[2][0] == board[1][1] == board[0][2]:
                declare_winner(board[2][0])

# CREATE THE TURN LOGIC FOR THE GAME
        while endloop == False and Count_Turns < 9:
        # Logic for knowing which is the team in control of the turn
            printboard()
            if Count_Turns % 2 == 0:
                current_team = Team_1 #Sets the team that is in charge during that turn
                symbol = home_team
            else:
                current_team = Team_2
                symbol = away_team
            player_name = input(f"\n{current_team}, pick a player to try and score: ").strip() # The function strip eliminates all the useless spaces to be able to compare the names directly to the dictionary
        # Check if the player picked is within the options in the dictionary
            if player_name not in player_to_cell:
                print("That player is not available for the game!. Choose another option")
                continue
        # Check that the player is picking an available cell, one that has not been used by the opponent
            chosen_cell = player_to_cell[player_name]
            if chosen_cell not in available_positions:
                print(f"That position {player_name} is already taken, a player has been used from there. Choose another cell.")
                continue
        # Modify the current state of the game board according to the input received, also checks if there has been a winning goal
            modgameboard(chosen_cell, symbol)
            available_positions.remove(chosen_cell)
            print(f"Incredible! {player_name} has scored an amazing goal for {current_team}!")
            checkwin(gameBoard)
            Count_Turns += 1

        if not endloop:
            print("It's a tie!")
            printboard()

#MAIN MENU for choosing the games
    print("Choose a game configuration:")
    print("1: Game 1")
    print("2: Game 2")
    print("3: Game 3")
    print("4: Game 4")
    choice = input("Enter the number of the game you want to play: ").strip()
    if choice == "1":
        row_labels, col_labels, player_to_cell = config_game1()
    elif choice == "2":
        row_labels, col_labels, player_to_cell = config_game2()
    elif choice == "3":
        row_labels, col_labels, player_to_cell = config_game3()
    elif choice == "4":
        row_labels, col_labels, player_to_cell = config_game4()
    else:
        print("Invalid choice. Defaulting to Game 1.")
        row_labels, col_labels, player_to_cell = config_game1()
    Team_1 = input("Team 1's name is: ")
    Team_2 = input("Team 2's name is: ")
    print(f"Let the championship final between {Team_1} and {Team_2} begin!")
    play_game(Team_1, Team_2, row_labels, col_labels, player_to_cell)

if __name__ == "__main__":
    Footy_tictactoe()
