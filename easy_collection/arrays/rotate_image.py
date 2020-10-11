"""
Given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

Rotate the image in-place, meaning modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Notes:
    matrix.length == n
    matrix[i].length == n
    1 <= n <= 20
    -1000 <= matrix[i][j] <= 1000

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
"""

from typing import *


def rotate(matrix: List[List[int]]) -> None:
    """
    In order to rotate the matrix 90 degrees, each element would need to be moved to the corresponding cell
    after a rotation. For example, an element in the 3rd position of the row from the left would end up in the
    3rd position of the column from the top in the column that it moves to.

    The way to do this would be to rotate each 'ring'.

    Each ring's movement can be summarized as:
        (i, j) -> (j, n-i) -> (n-i, n-j) -> (n-j, i) -> (i, j)

    Furthermore, if n is odd then the final 'ring' is simply the center cell and doesn't need to be moved. Hence,
    to iterate over the rings only requires going up to the floor(n/2) index.
    """

    n = len(matrix) - 1

    # Iterate over rings
    for i in range(int(n+1/2)):

        # Iterate over each quadruple of elements in the ring
        for j in range(i, n-i):
            tmp = matrix[n-j][i]
            matrix[n-j][i] = matrix[n - i][n - j]
            matrix[n - i][n - j] = matrix[j][n-i]
            matrix[j][n-i] = matrix[i][j]
            matrix[i][j] = tmp