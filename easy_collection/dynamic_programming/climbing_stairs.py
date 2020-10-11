"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Input: 3
Output: 3
"""

from typing import *


def climb_stairs(n: int) -> int:
    """
    Since we can climb either 1 or 2 stairs, then to get to the nth stair we can only go either from
    the (n-1)th stair or the (n-2)th stair. So the number of ways to get to the nth stair is the number
    of ways to get to the (n-1)th stair plus the number of ways to get to the (n-2)th stair.

    We can keep track of how many ways it takes to get to the previous 2 stairs to avoid recounting
    if we were to do this in a recursive method.
    """

    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        n_2 = 1
        n_1 = 2

        for i in range(3, n+1):
            n_1, n_2 = n_1 + n_2, n_1

        return n_1
