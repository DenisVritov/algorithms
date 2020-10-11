"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum
amount of money you can rob tonight without alerting the police.

Input: nums = [1,2,3,1]
Output: 4
"""

from typing import *


def max_theft(nums: List[int]) -> int:
    """
    To find the maximum amount that can be stolen we use the following formula:

    Given house number n (0-indexed),
    max_money(n) = max(
                        max_money(n-3) + n,
                        max_money(n-2) + n,
                        max_money(n-1)
                   )

    This is because as the thief, we would only ever skip over either 1 or 2 houses. If there were 3 houses we could
    hit up the middle house on the way without issue.

    Hence, we simply iterate over the given list and compute the maximum amount of stolen money that can be obtained
    if the list stopped at the house we are currently visiting. We can reuse the list to store the max values of
    previous sublists.
    """

    l = len(nums)

    if l == 0:
        return 0
    elif l == 1:
        return nums[0]
    elif l == 2:
        return max(nums)
    else:
        nums[2] = max(nums[1], nums[0] + nums[2])
        for i in range(3, len(nums)):
            nums[i] = max(nums[i-3] + nums[i], nums[i-2] + nums[i], nums[i-1])

        return nums[-1]
