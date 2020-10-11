"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII,
which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same
principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

Notes:

    1 <= s.length <= 15
    s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    It is guaranteed that s is a valid roman numeral in the range [1, 3999].

Input: s = "LVIII"
Output: 58
"""

from typing import *


def roman_to_integer(s: str) -> int:
    """
    This is a simple mapping problem. The only caveat is that we need to check whether the next symbol is greater than
    the current symbol in order to account for subtractions.

    Therefore, this is simply an iteration over the string with a lookahead pointer.
    """

    symbol_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    subtraction_map = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }

    if len(s) == 1:
        return symbol_map[s]

    ret = 0
    i = 0

    while i < len(s) - 1:
        if symbol_map[s[i]] < symbol_map[s[i+1]]:
            ret += subtraction_map[s[i:i+2]]
            i += 2
        else:
            ret += symbol_map[s[i]]
            i += 1

    if i < len(s):
        ret += symbol_map[s[-1]]

    return ret
