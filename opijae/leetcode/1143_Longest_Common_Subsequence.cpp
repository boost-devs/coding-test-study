#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <string>
using namespace std;
class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        vector<vector<int> > dp; // dp
        dp.resize(text1.length()+1, std::vector<int>(text2.length()+1, 0));
        // 2차원 벡터 크기 조절
        // vector<vector<int>> dp(n + 1, vector<int> (m + 1, 0));

        for (int i = 0; i < text1.length(); i++){
            for(int j = 0; j < text2.length(); j++){
                if (text1[i] == text2[j]){ // 같은 문자열이면 이전 까지 값 ++
                    dp[i+1][j+1] = dp[i][j] + 1;
                }
                else{ // 다른 문자열이면 지금까지 본 문자열 중 최대값
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j]);
                }
            }
        }
        return dp[text1.length()][text2.length()];
    }
};

int main(){
    Solution s;
    cout<<s.longestCommonSubsequence("abc","def");
}