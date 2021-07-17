/*
# DP
# Problem: 11055
# Memory: 2020KB
# Time: 0ms
*/
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int N, ret = 0;

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> N;
    vector<int> arr(N, 0);
    vector<int> dp(N, 0);
    for(int i = 0; i < N; i++) {
        cin >>arr[i];
        dp[i] = arr[i];
    }

    for(int i = N-1; i >= 0; i--){
        int tmp_max = 0;
        for (int j = i+1; j < N; j++) 
            if(arr[i] < arr[j]) dp[i] = max(dp[i], dp[j]+ arr[i]);
        ret = max(ret, dp[i]);
    }
    cout << ret << '\n';

    return 0;
}