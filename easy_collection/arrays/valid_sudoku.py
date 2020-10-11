"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
- Each row must contain the digits 1-9 without repetition
- Each column must contain the digits 1-9 without repetition
- Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition
- The Sudoku board could be partially filled, where empty cells are filled with the character '.'

Notes:
- A Sudoku board (partially filled) could be valid but is not necessarily solvable
- Only the filled cells need to be validated according to the mentioned rules
- The given board contain only digits 1-9 and the character '.'
- The given board size is always 9x9

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: True
"""

from typing import *


def is_valid_sudoku(board: List[List[str]]) -> bool:
    """
    There are 3 things that must be validated:
        - row
        - column
        - 3x3 box

    To do the check, we can utilize a single function that looks for duplicates given a list. For each
    row, column, and box we flatten the values into a single list (discarding ".") and pass to the function.
    """

    def flatten_row(row: List[str]) -> List[str]:
        return [element for element in row if element != "."]

    def check_duplicates(vals_list: List[str]) -> bool:
        vals_list.sort()
        for idx in range(len(vals_list) - 1):
            if vals_list[idx] == vals_list[idx + 1]:
                return True
        return False

    # Check rows
    for row in board:
        if check_duplicates(flatten_row(row)):
            return False

    # Check columns
    for idx in range(9):
        if check_duplicates(flatten_row([row[idx] for row in board])):
            return False

    # Check boxes
    for row_idx in range(0, 9, 3):
        for col_idx in range(0, 9, 3):
            row = []
            for row_step in range(3):
                row += board[row_idx+row_step][col_idx:col_idx+3]
            if check_duplicates(flatten_row(row)):
                return False

    return True
