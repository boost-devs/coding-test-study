"""
#  LeetCode
#  ver.Python3
#
#  Created by GGlifer
#
#  Open Source
"""

import sys
from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        idx = 1
        critical_points = []
        itr = head
        while itr and itr.next and itr.next.next:
            f, m, b = itr.val, itr.next.val, itr.next.next.val
            if (m < f and m < b) or (m > f and m > b):
                critical_points.append(idx)
            itr = itr.next
            idx += 1

        max_distance = -1
        min_distance = -1
        if len(critical_points) >= 2:
            max_distance = critical_points[-1] - critical_points[0]
            min_distance = sys.maxsize
            for i, j in zip(critical_points, critical_points[1:]):
                min_distance = min(min_distance, j-i)

        return [min_distance, max_distance]


def main():
    solution = Solution()

    def make_head(_lst: List):
        if not _lst:
            return None
        _head = itr = ListNode(_lst[0])
        for val in _lst[1:]:
            itr.next = ListNode(val)
            itr = itr.next
        return _head

    lst = [5, 3, 1, 2, 5, 1, 2]
    head = make_head(lst)

    print(solution.nodesBetweenCriticalPoints(head))


if __name__ == '__main__':
    main()
