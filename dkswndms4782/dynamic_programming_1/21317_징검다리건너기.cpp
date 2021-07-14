#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int N,a,b,k; cin >> N;
    int dp[30][2] = {0,};
    int jump[30][2];
    dp[1][1] = 9999999;
    fill(&dp[2][0], &dp[2][0] + 28 * 2, 9999999);
    for(int i = 1;i<N;i++) cin >> jump[i][0] >> jump[i][1];
    cin >> k;
    for(int i = 1;i<N;i++){
        dp[i + 1][0] = min(dp[i+1][0], dp[i][0] + jump[i][0]);
        dp[i + 2][0] = min(dp[i+2][0], dp[i][0] + jump[i][1]);
        dp[i + 3][1] = min(dp[i+3][1], dp[i][0] + k);
        dp[i + 1][1] = min(dp[i+1][1], dp[i][1] + jump[i][0]);
        dp[i + 2][1] = min(dp[i+2][1], dp[i][1] + jump[i][1]);
    }
    cout << min(dp[N][0], dp[N][1]);
}