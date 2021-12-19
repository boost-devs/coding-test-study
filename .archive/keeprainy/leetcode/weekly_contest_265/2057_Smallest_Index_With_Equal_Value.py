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
    def smallestEqual(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if i % 10 == n:
                return i
        return -1


def main():
    solution = Solution()

    nums = [0, 1, 2]

    print(solution.smallestEqual(nums))


if __name__ == '__main__':
    main()
