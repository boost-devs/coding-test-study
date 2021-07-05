/*
# DP
# Problem: 2156
# Memory: 2296KB
# Time: 0ms
*/
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int dp[3][10002] = {0, };

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    // input
    int N; cin >> N;
    vector<int> podo(N, 0);
    for(int i = 0; i < N; i++) cin >> podo[i];
    
    // init
    dp[1][0] = podo[0];

    // dp
    for(int i = 1; i < N; i++){
        dp[0][i] = max(dp[0][i-1], max(dp[1][i-1], dp[2][i-1]));
        dp[1][i] = dp[0][i - 1] + podo[i];
        dp[2][i] = dp[1][i - 1] + podo[i];
    }

    cout << max(dp[0][N-1], max(dp[1][N-1], dp[2][N-1]));

    return 0;
}