'''A monolithic and poorly written tic-tac-toe for you to refactor.'''
# Generated by ChatGPT 4
# Game state
p1 = "X"  # create a variable player 1
p2 = "O"  # create a variable player 2
empty = " "  # variable stores the symbol for an empty cell
board = [empty] * 9  # create a list with 9 elements default is empty

# Main Game loop that keeps game running until a win or tie
while True:
    # Print current state of the board - using 1D
    # refactor put in a module & use 2D data structure
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])
    print()

    # Check for win - put this within a class
    ''' 
    Defines a list of tuples called win_conditions 
    Each tuple contains three indices representing the positions on the board forming a winning combination
    The loop then checks if any of these combinations are filled with the same player's symbol and not empty
    Only considers if a player has filled three cells in a row, column, or diagonal with their symbol
    If a win condition is found, it prints the winner and exits the game
    '''
    win_conditions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for wc in win_conditions:
        if board[wc[0]] == board[wc[1]] == board[wc[2]] != empty:
            print("Player", board[wc[0]], "wins!")
            exit(0)

    # Check for tie  - put this within a class
    ''' 
    If there are no empty cells on the board = tie then prints "It's a tie!" and exits.
    exit(0) is an abrupt termination rewrite
    '''
    if empty not in board:
        print("It's a tie!")
        exit(0)

    # Get next move - put this within a class

    '''
    Gets next move from the current player. 
    Uses a while True loop to ensure the player provides a valid move
    Alternates between p1 and p2 based on the count of empty cells on the board
    Updates the board with the player's symbol if valid
    '''
    while True:
        player = p1 if board.count(empty) % 2 == 1 else p2
        move = input("Next move for player " + player + " (0-8): ")
        if move.isdigit() and 0 <= int(move) <= 8 and board[int(move)] == empty:
            board[int(move)] = player
            break
        else:
            print("Invalid move, try again.")
