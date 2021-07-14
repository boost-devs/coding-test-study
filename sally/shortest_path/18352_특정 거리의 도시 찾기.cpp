/*
# DP
# Problem: 18352
# Memory: 20436KB
# Time: 428ms
*/
#include <iostream>
#include <vector>
#include <cmath>
#include <queue>
#include <algorithm>
using namespace std;

int N, M, K, X;
vector<int> v[300002];
bool visit[300002] = {false,};
queue<int> q;
vector<int> ret;
int dep = 0;

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> N >>M >> K >>X;
    for(int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        v[a].push_back(b);
    }

    q.push(X);
    ret.push_back(X);
    visit[X] = true;

    while(!q.empty()){
        if(dep == K) break;
        ret.clear();
        int q_size = q.size();
        for(int t = 0; t < q_size; t++){
            int cur = q.front();
            q.pop();

            for(auto i: v[cur])
                if(visit[i] == false){
                    q.push(i);
                    visit[i] = true;
                    ret.push_back(i);
                }
                
        }
        dep++;
    }

    if(dep != K || ret.size() == 0) cout << -1;
    else{
        sort(ret.begin(), ret.end());
        for(auto i:ret)cout << i<<'\n';
    }

    return 0;
}