class Solution {
public:
    int smallestEqual(vector<int>& nums) {
        int num_len = nums.size();
        for(int i = 0 ; i < num_len; i++)
            if(i % 10 == nums[i])
                return i;
        return -1;
    }
};