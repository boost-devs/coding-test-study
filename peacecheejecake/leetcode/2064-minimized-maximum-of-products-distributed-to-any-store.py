from math import ceil


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        min_x, max_x = 1, max(quantities)
        while min_x < max_x:
            x = (min_x + max_x) // 2
            req_stores = sum([ceil(q / x) for q in quantities])
            if req_stores > n:
                min_x = x + 1
            elif req_stores <= n:
                max_x = x
        return min_x


# Runtime: 1872 ms
# Memory Usage: 28.3 MB
