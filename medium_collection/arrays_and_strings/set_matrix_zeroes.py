"""
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Constraints:
    m == matrix.length
    n == matrix[0].length
    1 <= m, n <= 200
    -2**31 <= matrix[i][j] <= 2**31 - 1

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
"""

from typing import *


def set_matrix_zeroes(matrix: List[List[int]]) -> None:
    """
    For this problem we need to keep track of which rows and columns must be set to zero. In order to do this
    efficiently we can keep track of that using the first element of each row and column since in the final matrix
    those values will be 0 if another element in its row or column is 0.

    In this way, we can use constant space. By nature of the problem, we must use at least O(mn) time since
    each element of the array must be checked.
    """

    first_row = False
    for j in range(len(matrix[0])):
        if matrix[0][j] == 0:
            first_row = True
            break

    first_col = False
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            first_col = True
            break

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, len(matrix)):
        if matrix[i][0] == 0:
            for j in range(1, len(matrix[0])):
                matrix[i][j] = 0

    for j in range(1, len(matrix[0])):
        if matrix[0][j] == 0:
            for i in range(1, len(matrix)):
                matrix[i][j] = 0

    if first_col:
        for i in range(len(matrix)):
            matrix[i][0] = 0

    if first_row:
        for j in range(len(matrix[0])):
            matrix[0][j] = 0
