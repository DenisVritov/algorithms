"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Input: [7,1,5,3,6,4]
Output: 5
"""

from typing import *


def max_profit(prices: List[int]) -> int:
    """
    Since we can only buy once and sell once, the max profit attainable would be finding the pair (a,b) where
    a comes before b and b-a yields the largest value of all pairs (a,b).

    Another way to think about this is for each index i, find the max value in prices[i+1:] such that the value is
    greater than prices[i].
    """

    profit = 0

    for i in range(1, len(prices)):
        profit = max(profit, prices[i] - prices[i-1])
        prices[i] = min(prices[i], prices[i-1])

    return profit
