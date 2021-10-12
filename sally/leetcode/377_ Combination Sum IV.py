# 377. Combination Sum IV
# Runtime: 67 ms, faster than 13.36% of Python3 online submissions for Combination Sum IV.
# Memory Usage: 14.2 MB, less than 70.21% of Python3 online submissions for Combination Sum IV.

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(1001)]
        dp[0] = 1
        for i in range(1, target+1):
            for j in nums:
                if i-j < 0: continue
                dp[i] += dp[i-j] 
        return dp[target];
        

# runtime error in cpp
# class Solution {
# public:
#     int combinationSum4(vector<int>& nums, int target) {
#         int dp[1002] = {0,};
#         dp[0] = 1;
#         for(int i = 1; i <= target; i++){
#             for(auto j : nums){
#                 int t = i - j;
#                 if(t < 0) continue;
#                 dp[i] += dp[t];
#             }
#         }
#         return dp[target];
#     }
# };