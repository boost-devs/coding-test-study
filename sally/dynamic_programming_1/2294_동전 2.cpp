/*
# DP
# Problem: 2294
# Memory: 2180KB
# Time: 0ms
*/
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

#define INF 1e9

int n, k;
int coin[101] = {0,};

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> n >> k;
    vector<int> dp(k+1, INF);
    for(int i = 0; i < n; i++){
        cin >> coin[i];
        dp[coin[i]] = 1;
    }

    for(int i = 1; i <= k; i++){
        for(auto j : coin){
            if(i + j <= k && dp[i] != INF){
                dp[i + j] = min(dp[i+j], dp[i] + 1);
            }
        }
    }

    if(dp[k] == INF) cout << "-1";
    else cout << dp[k];

    return 0;
}