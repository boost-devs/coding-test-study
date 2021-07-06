#include<iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int>v;
int dp[10002] = {-1,};

int main(){
    int N,K, tmp; cin >> N >> K;
    for(int i = 0;i<=K;i++) dp[i] = 10001;
    for(int i =0;i< N;i++) {
        cin >> tmp;
        v.push_back(tmp);
        if(tmp <= K) dp[tmp] = 1;
    }
    v.erase(unique(v.begin(), v.end()), v.end());
    for(int i = 0;i<v.size();i++){
        for(int j = v[i];j <= K;j++){
            if((j - v[i]) >= 0)
                dp[j] = min(dp[j-v[i]] + 1, dp[j]);
        }
    }
    if(dp[K] == 10001) cout << -1;
    else cout << dp[K];
}