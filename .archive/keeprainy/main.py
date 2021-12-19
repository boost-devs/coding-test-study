"""
#  LeetCode
#  ver.Python3
#
#  Created by GGlifer
#
#  Open Source
"""

from typing import *


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        dp = [0 for _ in range(target+1)]
        for num in nums:
            if num <= target:
                dp[num] += 1

        for i in range(2, target+1):
            for num in nums:
                if i-num >= 1:
                    dp[i] += dp[i-num]

        return dp[target]


if __name__ == '__main__':
    solution = Solution()

    nums = [4, 2, 1]
    target = 32

    print(solution.combinationSum4(nums, target))
