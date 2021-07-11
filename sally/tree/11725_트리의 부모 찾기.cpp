/*
# Tree
# Problem: 11725
# Memory: 9396KB
# Time: 72ms
*/
#include <iostream>
#include <string.h>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <algorithm>
#include <cmath>
#include <deque>
using namespace std;

int N;
queue<int> q;
vector<int>v [100001];
bool visit[100001] = {false, };
vector<pair<int, int>> result;


int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> N;
    for(int i = 0; i < (N-1); i++){
        int a, b;
        cin >> a >> b;
        v[a].push_back(b);
        v[b].push_back(a);
    }

    visit[1] = true;
    q.push(1);

    while(!q.empty()){
        int q_size = q.size();
        for(int t = 0; t < q_size; t++){
            int cur = q.front();
            q.pop();
            for(auto i: v[cur]){
                if(visit[i] == false){
                    visit[i] = true;
                    q.push(i);
                    result.push_back({i, cur});
                }
            }
        }
    }

    sort(result.begin(), result.end());
    for(auto i: result) cout << i.second << '\n';

    return 0;
}