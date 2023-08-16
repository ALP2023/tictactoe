'''
Print a game board using a 3x3 grid format
'''
#
#
# # by calculating indices explicitly - still in 1d structure
# def display_board_3x3(board):
#
#     for i in range(3):
#         print(board[i * 3], "|", board[i * 3 + 1], "|", board[i * 3 + 2])
#         if i < 2:
#             print("---------")
#

'''
Print a game board using a undefined grid format in 2D data structure
'''
def print_board(board):
    rows = [board[i:i + 3] for i in range(0, 9, 3)]
    board_str = "\n_________\n".join(" | ".join(row) for row in rows)
    print(board_str)




