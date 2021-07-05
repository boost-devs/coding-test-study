#include <iostream>
using namespace std;

#define MAX 1000000000
long long int dp[102][10] = {0,};


int main(){
    int N; cin >> N;
    for(int i = 1;i<=9;i++)
        dp[1][i] = 1;
    for(int i = 2;i<=N;i++){
        for(int j = 0;j<10;j++){
            if(j == 0)
                dp[i][j] = dp[i-1][1] % MAX;
            else if(j == 9)
                dp[i][j] = dp[i-1][8] % MAX;
            else
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1])% MAX;
        }
    }
    long long int result = 0;
    for(int i = 0;i<10;i++){
        result += dp[N][i];
        result %= MAX;
    }
    cout << result;
}