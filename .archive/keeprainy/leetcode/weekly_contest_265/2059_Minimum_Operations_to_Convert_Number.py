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


class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        dp = dict()
        que = deque()

        que.append(start)
        dp[start] = 0

        cnt = 0
        while que:
            r = len(que)
            for _ in range(r):
                c = que.popleft()
                if c == goal:
                    return dp[c]

                if 0 <= c <= 1000:
                    for num in nums:
                        for n in [c + num, c - num, c ^ num]:
                            if n not in dp:
                                dp[n] = dp[c] + 1
                                que.append(n)
            cnt += 1

        return -1


def main():
    solution = Solution()

    nums = [2, 8, 16]
    start = 0
    goal = 1

    print(solution.minimumOperations(nums, start, goal))


if __name__ == '__main__':
    main()
