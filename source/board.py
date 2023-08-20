
def print_board(board, rows, cols):
    '''
    Print a square game board using a 2D data structure
    '''
    for i in range(rows):
        row = board[i * cols:i * cols + cols]
        for j in range(len(row)):
            print(row[j], end="")
            if j < rows-1:
                print(" | ", end="")
        print()
        if i < rows-1:
            print("-" * (cols * 4 - 1))  # Print horizontal line

def create_board(rows, cols):
    return [[" " for _ in range(cols)] for _ in range(rows)]

def get_user_board_size():
    '''
    Get the desired board size between 3 and 20 from the user.

    Returns:
        rows, cols (int, int): The number of rows and columns for the game board.
    '''
    while True:
        try:
            rows = int(input("Enter your desired board size: "))
            cols = rows
            if 3 <= rows <= 20:
                return rows, cols
            else:
                print("Board size must be between 3 and 20.")
        except ValueError:
            print("Invalid input. Please enter a number > 2.")




