#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <string>
using namespace std;
// 2진수                                            || 1의 개수
// 0                        한 자리                 || 0
// 1                        한 자리                 || 1
// 10, 11                   두 자리                 || 1,2 => 반을 나눈다 (1),(2) => 오른쪽(2)는 왼쪽의 +1 이다.
// 100, 101, 110, 111       세 자리                 || 1,2,2,3 => 반을 나눈다 (1,2),(2,3) => 오른쪽(2,3)는 왼쪽의 +1 이다.
// 1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111   || 1,2,2,3,2,3,3,4 => 반을 나눈다 (1,2,2,3),(2,3,3,4) => 오른쪽(2,3,3,4)는 왼쪽의 +1 이다.
class Solution {
public:
    vector<int> countBits(int n) {
        // 0일때는 따로 빼줌
        if(n==0){
            vector<int> ans ={0};
            return ans;
        }
        int j =0;  // ans의 index
        int checkpoint = 2; // 2의 배수 마다 j를 0으로 초기화
        vector<int> ans ={0,1};// n==1일때 답
        for(int i=2; i<n+1; i++){
            if(i==checkpoint){
                j = 0;
                checkpoint *= 2;
            }
            ans.push_back(ans[j]+1);
            j++;
        }
        return ans;

    }
};

int main(){
    Solution s;
    vector<int> ans = s.countBits(1);
    for (auto& i : ans){
            cout<<i<<' ';
        }
}
