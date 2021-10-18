# 문제: 98. Validate Binary Search Tree
# 링크: https://leetcode.com/problems/validate-binary-search-tree/


# 시간/공간: 44ms / 16.4MB
# 참고: https://leetcode.com/problems/validate-binary-search-tree/discuss/32178/Clean-Python-Solution
class Solution:
    def isValidBST(
        self, root: Optional[TreeNode], floor=float("-inf"), ceiling=float("inf")
    ) -> bool:
        if not root:
            return True
        if root.val <= floor or root.val >= ceiling:
            return False
        return self.isValidBST(root.left, floor, root.val) and self.isValidBST(
            root.right, root.val, ceiling
        )
