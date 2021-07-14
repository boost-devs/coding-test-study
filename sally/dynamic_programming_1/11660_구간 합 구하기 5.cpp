/*
# DP
# Problem: 11660
# Memory: 10244KB
# Time: 140ms
*/
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int  n, m;
int a1, b1, a2, b2;
int arr[1026][1026] = {0,};
int dp[1026][1026] = {0,};

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> n >> m;
    for(int i = 1; i <= n;i ++)
        for(int j = 1; j <= n; j++){
            cin >> arr[i][j];
            arr[i][j] = arr[i][j-1] + arr[i][j]; 
        }

    for(int i = 1; i <= n;i ++)
        for(int j = 1; j <= n; j++)
            dp[i][j] = dp[i-1][j] + arr[i][j];
    
    while(m--){
        cin >> a1 >> b1 >> a2 >> b2;
        cout << dp[a2][b2] - dp[a1 - 1][b2] - dp[a2][b1 - 1] + dp[a1-1][b1-1] << '\n';
    }

    return 0;
}