
### Step 1: Review the Existing Code

Firstly, analyze the given tic-tac-toe game code. Understand the flow and functionality before proceeding with the refactoring.

See original tic_tac_o_oh.py code for comments.

Potential issues:
1.	The board is printed as a series of print functions
2.	Current implementation uses exit(0) to terminate the program when detected a winner or tie, which abruptly stops the program. 
3.	Can’t reset the board and play again once the game is over

Potential Solutions:
1.	Print the board as a 2D grid structure with cell label
2.	Use a quit function to end game i.e. ask the player(s) if they want to play again or quit
3.	Write a function to play multiple rounds without restarting the program

To further improve the game, refactor the code to include at least four functions, two classes, two files, and one import statement of your modules.

Module vs Classes: module = file containing related code and data that executes a single task well; whereas classes = blue print for creating objects and defines the structure and behaviour of objects based on that class.

•	Board printing

    o	should be a module as it only does one thing; i.e. print board
    o	use 2D data structure
    o	print the board in a 3x3 grid

Research: python - How do I create 3x3 matrices? - Stack Overflow & Python | Using 2D arrays/lists the right way - GeeksforGeeks.

•	Game (similar to Smiley assessment)

    o	contain classes for the game and players = game logic and player management
    o	unlike the Wordle assessment (where classes and game play were all in the main program), create a game module to contain classes for the game and players

