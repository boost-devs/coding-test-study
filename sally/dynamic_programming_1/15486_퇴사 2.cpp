/*
# DP
# Problem: 15486
# Memory: 19600KB
# Time: 228ms
*/
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    int N; cin >>N;
    vector<int> benefit(N+1, 0);
    vector<int> need(N+1, 0);
    vector<int> dp(N+1, 0);
    int result = 0;
    for(int i = 0; i <N; i++) cin >> need[i] >> benefit[i];

    for(int i = 0; i < N; i++){
        int target = i + need[i];
        dp[i] = max(result, dp[i]);
        if (target <= N)
            dp[target] = max(dp[target], dp[i]+benefit[i]);
        // for(auto j:dp) cout << j <<' ';
        // cout << '\n';
        result = max(result, dp[i]);
    }
    result = max(result, dp[N]);
    // if(need[N-1] == 1) result += benefit[N-1];

    cout << result;
    


    return 0;
}