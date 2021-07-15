/*
# DP
# Problem: 1106
# Memory: 2028KB
# Time: 0ms
*/
#include <iostream>
#include <cmath>
using namespace std;

#define INF 2147483646

int C; // goal
int N; // city num

int cost[201] = {0,};
int customer[201] = {0,};
int result = INF;

int dp[1001] = {0,}; // ind:customer val:min_cost

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    
    // input
    cin >> C >> N;
    for(int i = 0; i < C; i++) dp[i] = INF; // init
    for(int i = 0; i < N; i++){
        cin >> cost[i] >> customer[i];
        
        if(customer[i] >= C) result = min(result, cost[i]);
        else dp[customer[i]] = min(dp[customer[i]], cost[i]);
    }

    // process
    for(int i = 1; i < C; i++){
        if (dp[i] == INF) continue;
        // cout << dp[i] << '\n';
        for(int j = 0; j < N; j++){
            int ind = i + customer[j];
            if(ind >= C) result = min(result, dp[i]+cost[j]);
            else dp[ind] = min(dp[ind], dp[i] + cost[j]);
        }
    }

    cout << result;

    return 0;
}