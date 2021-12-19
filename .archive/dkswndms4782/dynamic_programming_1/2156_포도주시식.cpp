#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int n; cin >> n;
    int dp[10002]; int drink[10002];
    for(int i = 1;i<=n;i++) cin >> drink[i];
    dp[1] = drink[1]; dp[2] = drink[1] + drink[2];
    for(int i = 3;i<=n;i++){
        dp[i] = dp[i-1];
        dp[i] = max(dp[i], dp[i-2] + drink[i]);
        dp[i] = max(dp[i], dp[i-3] + drink[i] + drink[i-1]);
    }
    cout << dp[n];
}