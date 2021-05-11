/*
Graph Traversal - BFS, DFS
# Problem: 11725
# Memory: 8052KB
# Time: 52ms
# comment: 메모리 제대로 확인하기/간선의 수에 따른 자료구조 사용 필수
*/
#include <iostream>
#include <string.h>
#include <queue>
#include <vector>
using namespace std;

// 간선의 수가 작고 노드 수가 매우 크기 때문에 배열로 풀면 메모리 오류
// bool con[100001][100001] = {false, };
// int par[100001] = {0,};
queue<int> q;
int N;
int a, b;
int end_cnt = 1;

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    // init
    cin >> N;
    vector<vector<int>> con(N+1);
    vector<int> par(N+1, 0);

    for(int i = 0; i < N-1; i++){
        cin >> a >> b;
        con[a].push_back(b);
        con[b].push_back(a);
    }
    q.push(1);
    par[1] = 1;

    // BFS
    while(!q.empty()){
        if(end_cnt == N) break;
        int cur = q.front();
        q.pop();

        for(auto i: con[cur]) { // connected
            if (par[i] == 0) { // visit(x)
                par[i] = cur;
                q.push(i);
                end_cnt++;
            }
        }
    }

    for(int i = 2; i <= N; i++){
        cout << par[i] <<'\n';
    }


    return 0;
}