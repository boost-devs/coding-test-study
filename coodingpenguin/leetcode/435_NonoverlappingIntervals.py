# 문제: 435. Non-overlapping Intervals
# 링크: https://leetcode.com/problems/non-overlapping-intervals/


# 시간/공간: 1432ms / 52.4MB
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], x[0]))
        count = 0
        pred = -5 * int(1e4)
        for start, end in intervals:
            if pred <= start:
                pred = end
                count += 1
        return len(intervals) - count
