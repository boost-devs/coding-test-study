from collections import deque

class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        memo = {start}
        queue = deque([(start, 0)])
        while queue:
            x, deg = queue.popleft()
            if x < 0 or x > 1000:
                continue
            new_nums = set()
            for num in nums:
                cands = x + num, x - num, x ^ num
                for n in cands:
                    if n == goal:
                        return deg + 1
                    
                    if n not in memo:
                        new_nums.add((n, deg + 1))
                        memo.add(n)
                        
            queue.extend(new_nums)
        return -1
            