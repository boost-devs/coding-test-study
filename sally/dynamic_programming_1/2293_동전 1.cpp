/*
# DP
# Problem: 2293
# Memory: 2060KB
# Time: 0ms
*/
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int n, k;
int dp[10001] = {0,};
int coin[101] = {0,};

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> n >> k;
    for(int i = 0; i < n; i++) cin >> coin[i];
    dp[0] = 1;

    for(int i = 0; i < n; i++)
        for(int j = 1; j <= k; j++)
            if (0 <= j - coin[i]) dp[j] += dp[j - coin[i]];

    cout << dp[k];

    return 0;
}