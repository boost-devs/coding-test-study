/*
Graph Traversal - BFS, DFS
# Problem: 1260
# Memory: 21568KB
# Time: 12ms
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
bool visited[2][1001][10001] = {false, };
int a, b;
queue<int> q;

/* DFS func */
void DFS(int v){
    cout << v << " ";
    for(int i = 1; i <= N; i++){
        if (visited[0][i][v] == true || visited[0][v][i] == true) {
            if(visited[0][i][i] == false){
                visited[0][i][v] = visited[0][v][i] = false;
                visited[0][i][i] = true;
                DFS(i);
            }
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
            if (visited[1][i][cur] == true || visited[1][cur][i] == true)
            {
                if (visited[1][i][i] == false)
                {
                    visited[1][i][cur] = visited[1][cur][i] = false;
                    visited[1][i][i] = true;
                    q.push(i);
                }
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
        visited[0][a][b] = visited[0][b][a] = true; // DFS
        visited[1][a][b] = visited[1][b][a] = true; // BFS
    }

    visited[0][start_v][start_v] = visited[1][start_v][start_v] = true; 

    DFS(start_v);
    cout << '\n';
    BFS();
    cout << '\n';

    return 0;
}