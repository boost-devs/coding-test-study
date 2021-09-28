// 217. Contains Duplicate (Easy)
// Runtime: 16 ms, faster than 97.40% of C++ online submissions for Contains Duplicate.
// Memory Usage: 15.5 MB, less than 84.13% of C++ online submissions for Contains Duplicate.

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int N = nums.size();
        if(N == 1) return false;
        for(int i = 1; i < N; i++)
            if(nums[i-1] == nums[i]) return true;
        return false;
    }
};