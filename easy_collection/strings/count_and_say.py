"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
This can be done recursively, in other words from the previous member read off the digits, counting the
number of digits in groups of the same digit.

Note:
    Each term of the sequence of integers will be represented as a string.

Input: 4
Output: "1211"
"""

from typing import *


def count_and_say(n: int) -> str:

    if n == 1:
        return '1'

    s = count_and_say(n-1)
    ret = []
    count = 1
    num = s[0]
    for idx in range(1, len(s)):
        if s[idx] == num:
            count += 1
        else:
            ret.append(str(count))
            ret.append(num)
            count = 1
            num = s[idx]
    ret.append(str(count))
    ret.append(num)

    return ''.join(ret)
