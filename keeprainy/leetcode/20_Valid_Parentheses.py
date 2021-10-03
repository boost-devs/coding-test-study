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
    def isValid(self, s: str) -> bool:
        # Square bracket []
        # Curly bracket {}
        # Parentheses ()
        pair = {')': '(', '}': '{', ']': '['}

        st = []  # stack

        for b in s:
            if b in ['(', '{', '[']:
                st.append(b)
            else:
                if not st or st[-1] != pair[b]:
                    return False
                st.pop()

        return len(st) == 0


if __name__ == '__main__':
    solution = Solution()

