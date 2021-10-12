from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    # ref https://leetcode.com/problems/reorder-list/discuss/801971/Python-O(n)-by-two-pointers-w-Visualization
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None

        fast, slow = head, head # fast는 두칸 씩가고 slow는 한칸 씩 간다. 그러다 fast가 끝 점에 도달 했다면 slow는 자연스럽게 중간 까지 가게 된다.

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        mid = slow # 중간 점(끝점)

        prev, cur = None, mid
        # 중간을 기준으로 뒤집는다.
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        
        head_of_second_rev = prev

        first, second = head, head_of_second_rev
        # head -> head_of_second_rev -> head.. 순으로 reorder 해줌
        while second.next:
            
            next_hop = first.next
            first.next = second
            first = next_hop
            
            next_hop = second.next
            second.next = first
            second = next_hop