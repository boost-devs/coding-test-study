"""
#  LeetCode
#  ver.Python3
#
#  Created by GGlifer
#
#  Open Source
"""

from typing import *
from collections import deque
from itertools import accumulate


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        # i+nums[i] -> max idx with index i can reach
        # dp[i] -> max idx with index 0~i can reach
        dp = [i+nums[i] for i in range(len(nums))]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i], dp[i-1])

        # Jump!!!
        idx = 0
        while idx < len(nums) and idx < dp[idx]:
            idx = dp[idx]

        # Check max idx with can reach is more than last idx
        return bool(idx >= len(nums)-1)


if __name__ == '__main__':
    solution = Solution()

    nums = [3, 2, 1, 0, 4]

    solution.canJump(nums)
