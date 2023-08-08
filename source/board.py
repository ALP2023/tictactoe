'''
Print a game board using a 3x3 grid format in 2D data structure
'''


# by calculating indices explicitly
def display_board(board):

    for i in range(3):
        print(board[i * 3], "|", board[i * 3 + 1], "|", board[i * 3 + 2])
        if i < 2:
            print("---------")







