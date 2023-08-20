Once you have completed your refactoring, write a brief report addressing the following:

1. Justification for your refactoring decisions.

I have two modules, board.py and game.py, where the board.py is a module that only handles printing of the board and the game.py module handles all the game play associated with tic-tac-toe. Thus, leaving my main.py program to only handle a limited number of lines of code. This satisfies the requirements of Separation of Concerns where different aspects of a program should be handled separately, making the code easier to understand, modify, and maintain. 

My board.py module focuses on managing the game board and user input for board size, where the print_board() function handles the display of the game board, capturing the logic for printing a 2D board. The create_board() function creates a 2D board data structure with a specified number of rows and columns, whereas the get_user_board_size() function handles user input for board size, and handles invalid inputs (e.g., non-integer values or values less than or equal to zero) by catching ValueError exceptions and providing an error message. 

The game.py module is responsible for the game's core logic and player management. The TicTacO class encapsulates the game logic, and the methods within define different aspects of the game logic. In the make_move() method it checks if the input move is a valid integer within the bounds of the board and if the chosen cell is empty. If not, it returns False to indicate an invalid move. Whereas the Player class encapsulates player information, such that each player is represented with their symbol. This ensures that game-related logic is encapsulated within classes, following OOP principles.

The main.py program only has the play_game() function which arranges the game's flow. Using __name__ == "__main__" ensures that the code within this block only runs when the script is executed directly, not when it's imported as a module.


2. The challenges you would have faced maintaining and testing the original monolithic code.

•	Code readability and maintenance - code is written as a single, long block, making it difficult to read and maintain, especially if it expands.

•	The game board is a series of print functions repeated multiple times, i.e. code duplication. This means it needs to be updated in multiple if changes the way the board is displayed is desired. 

•	The win_conditions is hard-coded, making it less maintainable. This goes against the principles of separation of concerns and flexibility. 

•	To modify the game to have different board sizes or rules, requires extensive code changes because the game board and win_conditions are hardcoded, i.e. hard to scale and inflexible.

•	Can't reuse any of the code in other similar projects because it's highly specific to this particular game. 

•	Not much error handling within the code, with only simple print statements to deal with invalid input.

•	Testing will be complex and tricky, as isolating and testing individual components is difficult as the different functionalities are coupled. 

•	In the original code, game logic, user input/output, and win checking are all intermingled, violating the principle of Separation of Concerns and does not follow OOP principles.

3. How you would modify your refactored code to handle a custom-sized tic-tac-toe game (larger than 3x3), and how this implementation would be easier to handle than in the original code.

To create an expandable square board, you can modify the function to take the number of rows and columns as parameters. This way there is no refactoring required every time the game board changes size. I did this by replacing hard-wired values in my original code, which only handled a 3x3 grid, to taking rows and cols defined by the user in the get_user_board_size() function.

Original 3x3 2D grid:
def print_board(board):
    for i in range(3):
        row = board[i * 3:i * 3 + 3]  # Extract a row of 3 elements
        for j in range(len(row)):
            print(row[j], end="")
            if j < 2:
                print(" | ", end="")
        print()
        if i < 2:
            print("-" * 9)  # Print horizontal line
