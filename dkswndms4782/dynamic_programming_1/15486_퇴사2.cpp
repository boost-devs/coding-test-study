#include <iostream>
#include <algorithm>
using namespace std;
int T[1500002]; int P[1500002];

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N,a,b; cin >> N;
    for(int i = 1;i<=N;i++){
        cin >> a >> b;
        T[i] = a;
        P[i] = b;
    }
    int dp[1500002] = {0,};
    for(int i = 1;i<=N;i++){
        if((i + T[i]) <= N+1)dp[i + T[i]] = max(dp[i] + P[i], dp[i + T[i]]);
        dp[i+1] = max(dp[i+1], dp[i]);
    }
    cout << dp[N+1];
}