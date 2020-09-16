"""
Say you have an array prices for which the ith element is the price of a
given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many
transactions as you like (i.e., buy one and sell one share of
the stock multiple times).

Note: You may not engage in multiple transactions at the same time
(i.e., you must sell the stock before you buy again).

1 <= prices.length <= 3 * 10 ^ 4
0 <= prices[i] <= 10 ^ 4

Input: [7,1,5,3,6,4]
Output: 7
"""

from typing import *


def max_profit(prices: List[int]) -> int:
    """
    Since there is no penalty for selling then buying on the same day,
    we can treat each day-to-day as a discrete decision.

    If tomorrow's price is higher than today's, I buy now and sell tomorrow
    for a profit. Otherwise I don't buy today. Repeat for each day. Max profit
    is the sum of all discrete greedy decisions.
    """

    if len(prices) < 2:
        return 0

    profit = 0
    prev_price = prices[0]

    for idx in range(1, len(prices)):
        diff = prices[idx] - prev_price
        prev_price = prices[idx]
        if diff > 0:
            profit += diff

    return profit
