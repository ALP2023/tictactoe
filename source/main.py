'''
The play_game function in main.py orchestrates the game's flow
i.e.implement the main game loop and ask players if they want to play again or quit
'''

import board
from game import TicTacO, Player

def play_game():
    '''
    Orchestrates the Tic-Tac-Toe game.
    '''
    # Ask the user for board size
    rows, cols = board.get_user_board_size()

    # creating an instance of the TicTacO class = access to methods of the class
    game = TicTacO(rows, cols)

    player1 = Player("X")  # instance of Player class with X symbol
    player2 = Player("O")  # instance of Player class with O symbol

    game_board = board.create_board(rows, cols)

    # calling methods of the Tic-Tac-O class
    game.game_play()

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == "y":
        game.reset_board()
        play_game()

if __name__ == "__main__":
    play_game()

