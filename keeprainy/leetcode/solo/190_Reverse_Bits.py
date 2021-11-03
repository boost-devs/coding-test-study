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
    def reverseBits(self, n: int) -> int:
        # get binary string = bin(n)[2:]
        # reverse string = ''.join(reversed(...))
        # transform int = int(..., 2)
        return int(''.join(reversed(bin(n)[2:].zfill(32))), 2)


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseBits(4294967293))
