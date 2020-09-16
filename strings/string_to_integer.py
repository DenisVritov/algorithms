"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace
character is found. Then, starting from this character, takes an optional initial plus or minus sign
followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are
ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if
no such sequence exists because either str is empty or it contains only whitespace characters,
no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:
    - Only the space character ' ' is considered as whitespace character.
    - Assume we are dealing with an environment which could only store integers within the 32-bit signed
      integer range: [−2**31,  2**31 − 1]. If the numerical value is out of the range of representable values,
      INT_MAX (2**31 − 1) or INT_MIN (−2**31) is returned.

Input: "   -42"
Output: -42
"""

from typing import *


def atoi(s: str) -> int:
    """
    There are a lot of cases to cover with this function.

    Ideally the function would work as follows:
        - Strip out any white space at front of string
        - If encounter anything other than a digit, '+', or '-' return 0
        - If encounter '+' or '-' keep track of sign
        - Gather consecutive digits into 1 substring
        - Convert to integer
        - Check overflow bounds

    This function will not use the built-in int() function to convert the integer string since
    that defeats the point of this excercise. It will utilize the ord() function instead
    """

    if len(s) == 0:
        return 0

    index = 0
    while index < len(s) and s[index] == ' ':
        index += 1

    if index >= len(s):
        return 0

    sign = 1

    if not '0' <= s[index] <= '9':
        if s[index] == '+':
            index += 1
        elif s[index] == '-':
            sign = -1
            index += 1
        else:
            return 0

    ret = 0
    while index < len(s) and '0' <= s[index] <= '9':
        ret = ret * 10 + ord(s[index]) - ord('0')
        index += 1

    ret = sign * ret

    if ret > 2147483647:
        return 2147483647
    elif ret < -2147483648:
        return -2147483648
    else:
        return ret