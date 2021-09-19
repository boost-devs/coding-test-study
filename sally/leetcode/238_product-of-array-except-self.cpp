// 238. Product of Array Except Self (Medium)
// Runtime: 32 ms, faster than 24.58% of C++ online submissions for Product of Array Except Self.
// Memory Usage: 28 MB, less than 6.88% of C++ online submissions for Product of Array Except Self.

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> answer;
        vector<int> lefts, rights;
        int N = nums.size();
        lefts.push_back(1);
        rights.push_back(1);
        for(int i = 1; i < N; i++){
            lefts.push_back(lefts[i-1] * nums[i-1]);
            rights.push_back(rights[i-1] * nums[N-1-(i-1)]);
        }
        for(int i = 0; i < N; i++)
            answer.push_back(lefts[i] * rights[N-1-i]);
        return answer;
    }
};
