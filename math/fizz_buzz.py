"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five
output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
"""

from typing import *


def fizz_buzz(n: int) -> List[str]:
    """
    There are multiple ways of doing this but the premise is:
        - Check if number is divisible by 3, 5, or 15
        - Output appropriate response
    """

    ret = []

    for i in range(1, n+1):
        if i % 15 == 0:
            ret.append("FizzBuzz")
        elif i % 3 == 0:
            ret.append("Fizz")
        elif i % 5 == 0:
            ret.append("Buzz")
        else:
            ret.append(str(i))

    return ret
