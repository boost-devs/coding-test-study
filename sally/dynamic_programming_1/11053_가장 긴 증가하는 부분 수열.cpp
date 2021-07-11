/*
# DP
# Problem: 11053
# Memory: KB
# Time: ms
*/
#include <iostream>
#include <string>
#include <string.h>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <cmath>
using namespace std;

int N;
int arr[1001] = {0,};
int dp[1001] = {0,};
int ret = 1;

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> N;
    for(int i = 0; i < N; i++)
        cin >> arr[i];
    dp[N-1] = 1;

    int t = N-1;
    while(t--){
        int tmp_max = 1;
        for(int i = t+1; i < N; i++){
            if(arr[i] > arr[t])
                tmp_max = max(tmp_max, dp[i]);
        }
        dp[t] = tmp_max;
    }

    cout << dp[0];
    
    return 0;
}