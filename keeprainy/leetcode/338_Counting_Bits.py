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
    def countBits(self, n: int) -> List[int]:
        return [bin(i)[2:].count('1') for i in range(n+1)]


if __name__ == '__main__':
    solution = Solution()
