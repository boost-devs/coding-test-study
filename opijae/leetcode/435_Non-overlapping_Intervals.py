from typing import *

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key= lambda x: x[1]) # 끝나는 시점으로 정렬
        cnt = 1 # 제일 처음 빨리 끝나는 것 cnt
        cur = sorted_intervals[0] # 끝나는 시간 중 제일 빨리 끝나는 값 부터 시작
        for interval in sorted_intervals:
            if cur[1]<=interval[0]: # 다음 interval이 현재 interval보다 늦게 끝나면 cnt ++
                cnt +=1
                cur = interval
        return len(sorted_intervals) - cnt # 전체 interval에서 되는 interval 빼기
intervals = [[1,2],[2,3],[3,4],[1,3]]

a = Solution()
a.eraseOverlapIntervals(intervals)