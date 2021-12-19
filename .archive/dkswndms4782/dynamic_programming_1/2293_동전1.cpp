#include<iostream>
using namespace std;

int coin[101];
int dp[10002];

int main(){
    int N,K; cin >> N >> K;
    for(int i = 1;i<= N;i++) cin >> coin[i];
    dp[0] = 1;
    for(int i = 1;i<=N;i++){
        for(int j = coin[i];j <= K;j++){
            dp[j] += dp[j-coin[i]];
        }
    }
    cout << dp[K];
}