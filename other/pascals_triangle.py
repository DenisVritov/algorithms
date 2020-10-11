"""
Given a non-negative integer n, generate the first n rows of Pascal's triangle.

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

from typing import *


def pascals_triangle(n: int) -> List[List[int]]:
    """
    This can be done by creating each row by referencing the values from the previous row.
    """

    ret = []
    for row_num in range(n):
        new_row = [1]
        for i in range(row_num-1):
            new_row.append(ret[row_num-1][i] + ret[row_num-1][i+1])
        if row_num > 0:
            new_row.append(1)
        ret.append(new_row)

    return ret
