// 128. Longest Consecutive Sequence
// Runtime: 57 ms, faster than 85.98% of C++ online submissions for Longest Consecutive Sequence.
// Memory Usage: 22.3 MB, less than 97.56% of C++ online submissions for Longest Consecutive Sequence.

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        nums.erase(unique(nums.begin(), nums.end()), nums.end());
        int n_len = nums.size();
        int result = 1;
        int max_len = 1;
        for(int i = 1; i < n_len; i++){
            if(nums[i-1]+1 == nums[i]) max_len++;
            else {
                result = max(max_len, result);
                max_len = 1;
            }
        }
        result = max(max_len, result);
        if(n_len == 0) result = 0;
        return result;
    }
};