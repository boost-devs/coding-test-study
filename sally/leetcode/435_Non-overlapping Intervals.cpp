// 435. Non-overlapping Intervals
// Runtime: 416 ms, faster than 63.83 % of C++ online submissions for Non - overlapping Intervals.
// Memory Usage : 89.8 MB, less than 47.00 % of C++ online submissions for Non - overlapping Intervals.
// ref: https://leetcode.com/problems/non-overlapping-intervals/discuss/1520653/C%2B%2B-Sorting

class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        int end_point = intervals[0][1];
        int ans = 0;
        int intervals_len = intervals.size();
        for (int i = 1; i < intervals_len; i++) {
            if (intervals[i][0] < end_point) {
                ans++;
                end_point = min(end_point, intervals[i][1]);
            }
            else end_point = intervals[i][1];
        }
        return ans;
    }
};