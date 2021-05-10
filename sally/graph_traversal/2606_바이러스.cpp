/*
Graph Traversal - BFS, DFS
# Problem: 2606
# Memory: 2028KB
# Time: 0ms
*/
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <queue>
using namespace std;

bool coms[101][101] = {false, };
int num_com = 0;
int N = 0;
int a, b;
int result = 0;
queue<int> q;

int main(){
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> num_com >> N;
    for (int i = 0; i < N; i++) {
        cin >> a >> b;
        coms[a][b] = coms[b][a] = true;
    }

    coms[1][1] = true;
    q.push(1);
    
    while(!q.empty()){
        int cur = q.front();
        q.pop();

        for(int i = 1; i <= num_com; i++){
            if(i == cur) continue;
            if (coms[cur][i] == true && coms[i][i] == false) {
                q.push(i);
                // coms[cur][i] = coms[i][cur] = false;
                coms[i][i] = true;
                result++;
            }
        }
    }
    
    cout << result << '\n';

    return 0;
}