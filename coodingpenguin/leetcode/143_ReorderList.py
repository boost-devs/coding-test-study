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
