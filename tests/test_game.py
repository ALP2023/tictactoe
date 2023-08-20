import unittest

import sys
sys.path.append('../source_directory')  # Add the path to your source directory

# Import the class containing the check_win method from game.py
from game import TicTacO

class TestCheckWin(unittest.TestCase):

    def setUp(self):
        # Create an instance of YourTicTacToeClass
        self.game = TicTacO(3, 3)

    def test_row_all_X(self):
        self.game.board = ["X", "X", "X", "O", " ", "O", "O", "X", " "]
        self.assertEqual(self.game.check_win(), "X")

    def test_row_all_O(self):
        self.game.board = ["O", "O", "O", "X", " ", "X", "X", "O", " "]
        self.assertEqual(self.game.check_win(), "O")

    def test_row_2_X_and_1_blank(self):
        self.game.board = ["X", "X", " ", "O", " ", "O", "O", "X", " "]
        self.assertIsNone(self.game.check_win())

    def test_col_all_X(self):
        self.game.board = ["X", "O", "O", "X", "X", "O", "X", "O", "O"]
        self.assertEqual(self.game.check_win(), "X")

    def test_col_all_O(self):
        self.game.board = ["O", "X", "X", "O", "O", "X", "O", "X", "X"]
        self.assertEqual(self.game.check_win(), "O")

    def test_col_2_X_and_1_blank(self):
        self.game.board = ["X", "O", "X", "O", " ", "X", "X", "O", " "]
        self.assertIsNone(self.game.check_win())

    def test_left_diagonal_all_X(self):
        self.game.board = ["X", "O", "O", "X", "X", "O", "O", "O", "X"]
        self.assertEqual(self.game.check_win(), "X")

    def test_right_diagonal_all_O(self):
        self.game.board = ["O", "O", "X", "X", "O", "O", "X", "O", "O"]
        self.assertEqual(self.game.check_win(), "O")

    def test_left_diagonal_2_X_and_1_blank(self):
        self.game.board = ["X", "O", "O", "X", "X", "O", "O", "O", " "]
        self.assertIsNone(self.game.check_win())

if __name__ == '__main__':
    unittest.main()
