// 1. Two Sum (Easy)
// Runtime: 424 ms, faster than 16.26% of C++ online submissions for Two Sum.
// Memory Usage: 10.1 MB, less than 79.56% of C++ online submissions for Two Sum.

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int N = nums.size();
        bool success = false;
        vector<int> answer;
        for(int i = 0; i < N; i++)
            for(int j = i+1; j < N; j++)
                if(nums[i]+nums[j] == target) {
                    answer.push_back(i);
                    answer.push_back(j);
                }
        return answer;       
    }
};