/*
# DP
# Problem: 1890
# Memory: 2140KB
# Time: 0ms
*/
#include <iostream>
using namespace std;

int N;
int arr[101][101] = {0, };
long long int dp[101][101] = {0, };

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> N;
    dp[0][0] = 1;
    for(int i = 0; i < N; i++)
        for(int j = 0; j < N; j++){
            cin >> arr[i][j];
            if(arr[i][j] == 0) continue;
            int target1 = i + arr[i][j];
            int target2 = j + arr[i][j];
            if (target1 < N) dp[target1][j] = dp[target1][j] + dp[i][j];
            if (target2 < N) dp[i][target2] = dp[i][target2] + dp[i][j];
        }

    cout << dp[N-1][N-1];

    return 0;
}