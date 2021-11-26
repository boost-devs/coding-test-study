"""
#  LeetCode
#  ver.Python3
#
#  Created by GGlifer
#
#  Open Source
"""

from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        trace = []

        def travel(c: TreeNode) -> bool:
            if c.left is not None:
                travel(c.left)
            trace.append(c.val)
            if c.right is not None:
                travel(c.right)

        travel(root)  # inorder

        # inorder trace must be monotone increasing
        for a, b in zip(trace, trace[1:]):
            if not a < b:
                return False
        return True


if __name__ == '__main__':
    lst = [5, 4, 6, None, None, 3, 7]

    def make_node(c):
        node = TreeNode(lst[c])
        n = 2*c+1
        if n < len(lst) and lst[n] is not None:
            node.left = make_node(n)
        n = 2*c+2
        if n < len(lst) and lst[n] is not None:
            node.right = make_node(n)
        return node

    root = make_node(0)

    solution = Solution()
    print(solution.isValidBST(root))
