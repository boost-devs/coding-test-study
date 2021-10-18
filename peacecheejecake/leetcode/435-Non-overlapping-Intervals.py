class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev = intervals[0]
        count = 0
        for s, e in intervals[1:]:
            sp, ep = prev
            if s < ep:
                count += 1
                prev = [s, e] if e < ep else prev
            else:
                prev = [s, e]
        return count
        