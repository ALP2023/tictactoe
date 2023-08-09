'''
Game logic and player management are handled by the TicTacToe and Player classes in game.py module.
'''

class TicTacO:
    def __init__(self):
        self.p1 = "X"
        self.p2 = "O"
        self.empty = " "
        self.board = [self.empty] * 9
        self.current_player = self.p1

    def check_win(self):
        ''' Check for win conditions and return the winner or None based on 1D structure'''
        win_conditions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for wc in win_conditions:
            if self.board[wc[0]] == self.board[wc[1]] == self.board[wc[2]] != self.empty:
                return self.board[wc[0]]
        return None

    def check_tie(self):
        ''' Check if the game is a tie '''
        return self.empty not in self.board

    def switch_player(self):
        ''' Switch the current player for the next turn '''
        self.current_player = self.p1 if self.current_player == self.p2 else self.p2

    def make_move(self, move):
        ''' Make a move for the current player '''
        if move.isdigit() and 0 <= int(move) <= 8 and self.board[int(move)] == self.empty:
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
