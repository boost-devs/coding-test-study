/*
Graph Traversal - BFS
# Problem: 14940
# Memory: 6916KB
# Time: 40ms
*/
#include <iostream> 
#include <string.h>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

int N, M;
pair<int, int> start_v;
int xy[4][2] = {{0, 1},{1, 0},{-1, 0},{0, -1},};
int map[1001][1001] = {0,};
bool visit[1001][1001] = {false, };
queue<pair<int, int>> q;

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    // input
    cin >> N >> M;
    for(int i = 0; i < N; i++)
        for(int j = 0; j < M; j++){
            int a; cin >> a;
            if(a == 2) start_v = make_pair(i, j);
            if(a == 0) visit[i][j] = true;
        }

    q.push(start_v);
    visit[start_v.first][start_v.second] = true;

    int dep = 0;
    while(!q.empty()){
        int q_size = q.size();
        for(int t = 0; t < q_size; t++){
            int x = q.front().first;
            int y = q.front().second;
            q.pop();
            map[x][y] = dep;

            for(int i = 0; i < 4; i++){
                int x_ = x + xy[i][0];
                int y_ = y + xy[i][1];
                if (0 <= x_ && x_ < N && 0 <= y_ && y_ < M)
                    if(visit[x_][y_] == false){
                        q.push({x_, y_});
                        visit[x_][y_] = true;
                    }
            }
        }
        dep++;
    }


    for(int i = 0; i < N; i++){
        for (int j = 0; j < M; j++) 
            if(visit[i][j] == false) cout << "-1 ";
            else cout << map[i][j] << ' ';
        cout <<'\n';
    }
        

    return 0;
}
