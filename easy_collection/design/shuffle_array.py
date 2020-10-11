"""
Shuffle a set of numbers without duplicates.

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
"""

from typing import *


class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums.copy()
        self.current = nums.copy()
        self.n = len(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        # Make sure to use copy() so that self.current is set to the values, not the reference
        self.current = self.original.copy()
        return self.current

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        import random

        for i in range(self.n-1, 0, -1):
            j = random.randint(0, i)
            self.current[i], self.current[j] = self.current[j], self.current[i]

        return self.current
