'''
main game loop is contained in the play_game() function in main.py
i.e.implement the main game loop and ask players if they want to play again or quit
'''

import board
from game import TicTacO, Player

def play_game():
    game = TicTacO()   # creating an instance of the TicTacO class = access to methods of the class8
    player1 = Player("X")  # instance of Player class with X symbol
    player2 = Player("O")  # instance of Player class with O symbol

    # game loop
    while True:
        print("It's", game.current_player, "'s turn.")
        board.display_board(game.board)  # from board module containing display_board function

    # calling methods of the Tic-Tac-O class
        if game.check_win():
            print("Player", game.check_win(), "wins!")
            break
        elif game.check_tie():
            print("It's a tie!")
            break

        move = input("Next move for player " + str(game.current_player) + " select 0-8 or 'q' to quit: ")
        if move.lower() == 'q':
            print("Thanks for playing. Good-bye!")
            break
        if not game.make_move(move):
            print("Invalid move, try again.")
            continue

        game.switch_player()

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == "y":
        game.reset_board()
        play_game()

if __name__ == "__main__":
    play_game()
