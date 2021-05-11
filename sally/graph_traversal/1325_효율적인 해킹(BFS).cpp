/*
Graph Traversal - BFS, DFS, Di-graph, Cycle Graph
# Problem: 1325
# Memory: 3224KB
# Time: 2632ms
*/
#include <iostream>
#include <string.h>
#include <vector>
#include <queue>
#include <algorithm>
#include <cmath>
using namespace std;

int N, M;
int a, b;
vector<vector<int>> con(10001);
bool visit[10001] = {false, };
int depths[10001] = {0, };
queue<int> q;

int BFS(int start_v){
    for(int i = 0; i <= N; i++) visit[i] = false;
    q.push(start_v);
    visit[start_v] = true;

    int ret = 1;
    while(!q.empty()){
        int cur = q.front();
        q.pop();

        int nex_size = con[cur].size();
        for(int i = 0; i < nex_size; i++){
            int nex = con[cur][i];
            if(visit[nex] == false){
                visit[nex] = true;
                q.push(nex);
                ret++;
            }
        }
    }

    return ret;
}

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    // init
    cin >> N >> M;

    for(int i = 0; i < M; i++){
        cin >> a >> b;
        con[b].push_back(a);
    }

    int max_ = 0;
    for(int i = 1; i <= N; i++){
        depths[i] = BFS(i);
        max_ = max(max_, depths[i]);
    }

    for(int i = 1; i <= N; i++){
        if(depths[i] == max_)
            cout << i << ' ';
    }
    
    return 0;
}