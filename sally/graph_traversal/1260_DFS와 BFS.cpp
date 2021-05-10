/*
Graph Traversal - BFS, DFS
# Problem: 1260
# Memory: 2996KB
# Time: 4ms
*/
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <queue>
#include <string.h>
using namespace std;

int N, M, start_v;
bool con[1001][1001] = {false, };
bool visited[1001] = {false, };
int a, b;
queue<int> q;

/* DFS func */
void DFS(int v){
    cout << v << ' ';

    for(int i = 1; i <= N; i++){
        if(v != i && con[i][v] == true && visited[i] == false){
            visited[i] = true;
            DFS(i);
        }
    }
}

/* BFS func */
void BFS(){
    q.push(start_v);

    while(!q.empty()){
        int cur = q.front();
        cout << cur << " ";
        q.pop();

        for(int i = 1; i <= N; i++){
            if(cur != i && con[cur][i] == true && visited[i] == false){
                visited[i] = true;
                q.push(i);
            }
        }
    }
}

int main(){
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    // init
    cin >> N >> M >> start_v;
    for(int i = 0; i < M; i++){
        cin >> a >> b;
        con[a][b] = con[b][a] = true;
    }

    visited[start_v] = true; 
    DFS(start_v);
    cout << '\n';

    memset(visited, false, sizeof(visited)); // visit init

    visited[start_v] = true;
    BFS();
    cout << '\n';

    return 0;
}