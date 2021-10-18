"""
#  LeetCode
#  ver.Python3
#
#  Created by GGlifer
#
#  Open Source
"""

from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def clone(node: ListNode):
    return ListNode(node.val, node.next)


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Reference
        # https://leetcode.com/problems/reorder-list/discuss/208984/Python-solution

        if not head or not head.next:
            return
        slow = head
        fast = head.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        slow = slow.next  # mid
        if fast.next:
            fast = fast.next  # tail

        # reverse tail ~ mid
        prev = slow
        curr = slow.next
        prev.next = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        itr1 = head  # head ~ mid
        itr2 = fast  # tail ~ mid
        while itr2.next:
            tmp1 = itr1.next
            tmp2 = itr2.next
            itr1.next = itr2
            itr2.next = tmp1
            itr1 = tmp1
            itr2 = tmp2


def main():
    lst = [1, 2, 3, 4, 5]
    head = itr = ListNode(lst[0])
    for v in lst[1:]:
        itr.next = ListNode(v)
        itr = itr.next

    solution = Solution()

    solution.reorderList(head)


if __name__ == '__main__':
    main()
