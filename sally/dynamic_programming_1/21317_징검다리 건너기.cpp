/*
# DP
# Problem: 21317
# Memory: 2020KB
# Time: 0ms
*/
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

#define INF 1e9

int n, k;
int energy[2][25] = {0,};
int dp[2][25];

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    // init
    cin >> n;
    for(int i = 0; i < n-1; i++)
        cin >> energy[0][i] >> energy[1][i];
    for(int i = 0; i < n; i++)
        dp[0][i] = dp[1][i] = INF;
    cin >> k;

    dp[0][0] = 0;
    // dp process
    for(int i = 0; i < n; i++){
        for (int j = 0; j < 2; j++)
            if(i + j + 1 < n)
                dp[0][i + j + 1] = min(dp[0][i + j + 1], dp[0][i] + energy[j][i]);
        if(2 < i)
            dp[1][i] = min(dp[1][i - 1] + energy[0][i - 1], min(dp[1][i - 2] + energy[1][i - 2], dp[0][i - 3] + k));
    }

    cout << min(dp[0][n-1], dp[1][n-1]);

    
    return 0;
}