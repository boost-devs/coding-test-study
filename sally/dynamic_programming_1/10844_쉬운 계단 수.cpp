/*
# DP
# Problem: 10844
# Memory: 2028KB
# Time: 0ms
*/
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

#define TOK 1000000000

int N;
long long int result = 0;
long long int dp[101][10] = {0,};

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> N;
    
    for(int i = 1; i <= 9; i++) dp[1][i] = 1;
    for(int i = 2; i <= N; i++) {
        dp[i][1] = dp[i - 1][0];
        dp[i][8] = dp[i - 1][9];
        for(int j = 1; j <= 8; j++){
            dp[i][j + 1] = (dp[i - 1][j] + dp[i][j + 1]) % TOK;
            dp[i][j - 1] = (dp[i][j - 1] + dp[i - 1][j]) % TOK;
        }
    }

    for(int i = 0; i <= 9; i++){
        result += dp[N][i];
        result %= TOK;
    }
        
    cout << result << '\n';

    return 0;
}