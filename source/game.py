'''
Game logic and player management are handled by the TicTacToe and Player classes in game.py module.
'''
import board
class TicTacO:
    def __init__(self, rows, cols):
        self.p1 = "X"
        self.p2 = "O"
        self.empty = " "
        self.rows = rows
        self.cols = cols
        self.board = [self.empty] * (rows * cols)
        self.current_player = self.p1

    def game_play(self):
        while True:
            print("It's", self.current_player, "'s turn.")
            board.print_board(self.board, self.rows, self.cols)

            if self.check_win():
                print("Player", self.check_win(), "wins!")
                break
            elif self.check_tie():
                print("It's a tie!")
                break

            move = input("Next move for player " + str(self.current_player) + " select 0-" + str(self.rows*self.cols-1) + " or 'q' to quit: ")
            if move.lower() == 'q':
                print("Thanks for playing. Good-bye!")
                break
            if not self.make_move(move):
                print("Invalid move, try again.")
                continue

            self.switch_player()
    def check_win(self):
        '''
        Check for win conditions and return the winner or None
        '''

        board = [self.board[i:i + self.cols] for i in range(0, len(self.board), self.cols)]

        # Check rows
        for row in board:
            if all(cell == "X" for cell in row):
                return "X"
            elif all(cell == "O" for cell in row):
                return "O"

        # Check columns
        for col in range(self.cols):
            if all(row[col] == "X" for row in board):
                return "X"
            elif all(row[col] == "O" for row in board):
                return "O"

        # Check diagonals (top-left to bottom-right)
        if all(board[i][i] == "X" for i in range(self.rows)) or all(board[i][i] == "O" for i in range(self.rows)):
            return board[0][0]

        # Check diagonals (top-right to bottom-left)
        if all(board[i][self.cols - 1 - i] == "X" for i in range(self.rows)) or all(
                board[i][self.cols - 1 - i] == "O" for i in range(self.rows)):
            return board[0][self.cols - 1]

        # No winner found
        return None

    def check_tie(self):
        ''' Check if the game is a tie '''
        return self.empty not in self.board

    def switch_player(self):
        ''' Switch the current player for the next turn '''
        self.current_player = self.p1 if self.current_player == self.p2 else self.p2

    def make_move(self, move):
        '''
        Make a move for the current player.

        Args:
            move (str): The move chosen by the player as a string.

        Returns:
            bool: True if the move is valid and successful, False otherwise.
        '''
        if move.isdigit() and 0 <= int(move) <= (self.rows * self.cols - 1) and self.board[int(move)] == self.empty:
            self.board[int(move)] = self.current_player
            return True
        else:
            return False

    def reset_board(self):
        ''' Reset the board for a new round '''
        self.board = [self.empty] * 9

# defines the player's symbol
class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def __str__(self):
        return self.symbol