# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        cps = []
        min_dist = 1e5
        prev, head = head.val, head.next
        i = 1
        while head.next is not None:
            if (head.val > prev and head.val > head.next.val or
                head.val < prev and head.val < head.next.val):
                if cps:
                    min_dist = min(min_dist, i - cps[-1])
                cps.append(i)
                    
            i += 1
            prev, head = head.val, head.next
        
        if len(cps) < 2:
            return [-1, -1]
        return [min_dist, cps[-1] - cps[0]]
    