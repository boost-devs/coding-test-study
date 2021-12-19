"""
#  LeetCode
#  ver.Python3
#
#  Created by GGlifer
#
#  Open Source
"""

import heapq
from typing import *


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Set is implemented in hashset at Python3
        s = set(nums)

        max_len = 0
        for e in s:
            if e-1 in s:  # Check e is first element in sequence
                continue
            else:
                tmp_len = 0
                while e in s:
                    tmp_len += 1
                    e += 1
                max_len = max(max_len, tmp_len)

        return max_len


if __name__ == '__main__':
    solution = Solution()
