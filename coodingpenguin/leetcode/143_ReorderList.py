# 문제: 143. Reorder List
# 링크: https://leetcode.com/problems/reorder-list/


# 시간/공간: 84ms / 23.3MB
# 참고: https://leetcode.com/problems/reorder-list/discuss/801883/Python-3-steps-to-success-explained


"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        hist = []
        current = head
        while current != None:
            hist.append(current)
            current = current.next

        pointer = head
        for _ in range(len(hist) // 2):
            _next = pointer.next
            pointer.next = hist.pop()
            pointer = pointer.next
            pointer.next = _next
            pointer = pointer.next

        if pointer != None:
            pointer.next = None
