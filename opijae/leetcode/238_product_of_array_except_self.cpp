#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <string>
using namespace std;


class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int _product = 1;
        int zero_cnt = 0;
        int length = nums.size();
        for(auto& i : nums) {
            if (i==0){
                zero_cnt++;
                if(zero_cnt==2){
                    vector<int> ans(length);
                    return ans;
                }
            }
            else{
                _product *= i;
            }
        }
        vector<int> ans;
        for (auto& i : nums){
            if (zero_cnt==1){
                if(i==0){
                    ans.push_back(_product);
                }
                else{
                    ans.push_back(0);
                }
            }
            else{
                ans.push_back( _product/i);
            }
        }
        return ans;
    }
};


// two pointers, 다른 코드 참조
class Solution1 {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans (n,1);
        int l = 1;
        int r = 1;
        for (int i = 0; i <n; i++){
            ans[i] * l;
            l *= nums[i];
            ans[n-i-1] *= r;
            r *= nums[n-i];
        }
        return ans;
    }
};


int main(){
    Solution s;
    vector<int> tmp = {1,2,3,4,0};
    vector<int> ans = s.productExceptSelf(tmp);
    for (auto& i : ans){
            cout<<i<<' ';
        }
}