from math import ceil


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        
        def _req_stores(x):
            return sum([ceil(q / x) for q in quantities])
        
        min_x, max_x = 1, max(quantities)
        while min_x < max_x - 1:
            x = (min_x + max_x) // 2
            req_stores = _req_stores(x)
            if req_stores > n:
                min_x = x
            elif req_stores <= n:
                max_x = x
        
        if _req_stores(min_x) > n:
            return max_x
        return min_x


# Runtime: 1772 ms
# Memory Usage: 28.6 MB
