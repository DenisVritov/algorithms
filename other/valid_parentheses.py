"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Input: s = "([)]"
Output: False
"""

from typing import *


def valid_parentheses(s: str) -> bool:
    """
    We can do this in a recursive manner by keeping track of the closing parenthesis we are looking for and
    calling the function recursively if we encounter something other than what we are looking for.

    Immediate false is if we find a closing parenthesis of a type other than the one that is being searched for
    in that iteration of the recursive function.
    """

    closing_map = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    stack = []

    for c in s:
        if c in closing_map:
            stack.append(closing_map[c])
        else:
            if not stack:
                return False
            elif c != stack.pop():
                return False

    if stack:
        return False

    return True
