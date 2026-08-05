game_board = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
num_list = [1,2,3,4,5,6,7,8,9]

Player_1_Marker = input("Player 1, choose your marker[X/O] : ")
if Player_1_Marker == "X":
    Player_2_Marker = "O"
else:
    Player_2_Marker = "X"

def save_game(board, filename = "Tic Tac Toe/saved_game.txt"):
    choice = input("Would you like to save the game? (Yes/No): ")
    if choice.lower() == "yes":
        with open('Tic Tac Toe/saved_game.txt', 'w') as i:
            for row in board:
                 i.write(",".join(row) + "\n")
        print("Game saved!")
    else:
        print("Okay! Continue Playing. ")

def load_game(filename="Tic Tac Toe/saved_game.txt"):
    loaded_board = []
    with open(filename, "r") as f:
        for line in f:
            row = line.strip().split(",")
            loaded_board.append(row)
    return loaded_board

option = input("Would you like to load the previous game? (Yes/No): ")
if option.lower() == "yes":
    print("Okay! Your previous game has been loaded!")
    game_board = load_game('Tic Tac Toe/saved_game.txt')

def display_board(game_board):
    for i in range(len(game_board)):
        for j in range(len(game_board)):
            game_board[i][j] = str(game_board[i][j])
        real_board = "|".join(game_board[i])
        print(real_board)
        print("-----")
display_board(game_board)

def check_tie(board):
    tie = False
    for value in range(len(board)):
        if value in num_list:
            tie = True
    return tie

def check_winner(board):
    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
        if Player_1_Marker == "X":
            print("Player 1 is the winner!")
            return True
    if board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
        if Player_1_Marker == "X":
            print("Player 1 is the winner!")
            return True
    if board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
        if Player_1_Marker == "X":
            print("Player 1 is the winner!")
            return True
    if board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        if Player_1_Marker == "X":
            print("Player 1 is the winner!")
            return True
    if board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
        if Player_1_Marker == "X":
            print("Player 1 is the winner!")
            return True
    if board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
        if Player_1_Marker == "X":
            print("Player 1 is the winner!")
            return True
    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        if Player_1_Marker == "X":
            print("Player 1 is the winner!")
            return True
    if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        if Player_1_Marker == "X":
            print("Player 1 is the winner!")
            return True
    return False

def play_game():
    coordinate_options = []
    player_1_turns = 9
    player_2_turns = 9
    while player_2_turns != 0:
        player_1_marker_placement = input("Player 1, where would you like to place your marker? [Row Number, Column Number]: ")
        player_1_marker_placement = player_1_marker_placement.split(",")
        coordinate_options.append(player_1_marker_placement)
        x = int(player_1_marker_placement[0])
        y = int(player_1_marker_placement[1])
        game_board[x - 1][y - 1] = Player_1_Marker
        display_board(game_board)
        player_1_turns -= 1
        print(f"Player 1 Turns Left: {player_1_turns}")
        if check_winner(game_board):
            return
        save_game(game_board, "saved_game.txt")

        player_2_marker_placement = input("Player 2, where would you like to place your marker? [Row Number, Column Number]: ")
        player_2_marker_placement = player_2_marker_placement.split(",")
        if player_2_marker_placement in coordinate_options:
            print("That's already taken. Please choose again:")
            choice = input("Player 2, where would you like to place your marker? [Row Number, Column Number]: ")
            player_2_marker_placement = choice.split(",")
        w = int(player_2_marker_placement[0])
        z = int(player_2_marker_placement[1])
        print(w, z)
        game_board[w - 1][z - 1] = Player_2_Marker
        display_board(game_board)
        player_2_turns -= 1
        print(f"Player 2 Turns Left: {player_2_turns}")
        if check_winner(game_board):
            return
        save_game(game_board, "saved_game.txt")

    tie = check_tie(game_board)
    if tie == True:
        print("The game is a TIE!")
    return

play_game()