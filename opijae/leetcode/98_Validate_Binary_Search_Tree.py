from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validBST(root, float('-inf'), float('inf'))
    def validBST(self, node, _min, _max):
        """
        Args:
            node : 현재 root node
            _min : 임계값(작은)
            _max : 임계값(큰)
        """
        if not node:
            return True
        
        if node.val <= _min or node.val >= _max:
            return False
        return self.validBST(node.left, _min, node.val) and self.validBST(node.right, node.val, _max)