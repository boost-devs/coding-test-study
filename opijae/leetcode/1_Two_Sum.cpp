#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <string>
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<vector<int>> idx_nums;
        for (int i = 0; i < nums.size(); i++) {
            vector<int> tmp;
            tmp.push_back(nums[i]);
            tmp.push_back(i);
            idx_nums.push_back(tmp);
        }
        sort(idx_nums.begin(),
            idx_nums.end(),
            [](const std::vector<int>& a, const std::vector<int>& b)
            {
                return a[0] < b[0];
            });
        int sum, s = 0, e = nums.size() - 1;
        sum = idx_nums[s][0] + idx_nums[e][0];
        vector<int> ans;
        while (s < e) {
            if (sum == target) {
                ans.push_back(idx_nums[s][1]);
                ans.push_back(idx_nums[e][1]);
                break;
            }
            else if (sum > target) {
                sum -= idx_nums[e][0];
                sum += idx_nums[--e][0];
            }
            else {
                sum -= idx_nums[s][0];
                sum += idx_nums[++s][0];
            }
        }
        return ans;
    }
};

int main(){
    Solution a;
    vector<int> tmp = {1,2,3};
    vector<int> ans = a.twoSum(tmp,4);
    for(auto& i:ans){
        cout<<i<<' ';
    }
}