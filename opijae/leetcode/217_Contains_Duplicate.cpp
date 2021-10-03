#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <string>
#include <set>
#include <map>
using namespace std;

//  SET 자료 구조 사용 후 길이 비교 48ms
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set<int> s ;
        for (auto& i:nums){
            s.insert(i);
        }
        if (s.size() != nums.size()){
            return true;
        }
        else{
            return false;
        }
    }
};


// map(python dict) 사용, arr 사요하려 했으나 숫자가 -10^9 ~ 10^9 라 ㅈㅈ
class Solution1 {
public:
    bool containsDuplicate(vector<int>& nums) {
        map<int,int> _dict{};
        for (int i=0; i <nums.size(); i++){
            if (_dict[nums[i]] ==0 ){
                _dict[nums[i]] += 1;
            }
            else{
                return true;
            }
        }
        return false;
    }
};


// sort 사용, 시간 제일 빠른 사람 코드
// sort가 nlogn아닌가... test 데이터 분포에 따라 다른걸까?
class Solution2 {
public:
    bool containsDuplicate(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        for(int i=0;i<nums.size()-1;i++){
            if(nums[i]==nums[i+1]){
                return true;
            }
        }
    return false;
    }
};


int main(){
    Solution1 s;
    vector<int> tmp = {2,14,18,22,22};
    cout<<s.containsDuplicate(tmp);
}