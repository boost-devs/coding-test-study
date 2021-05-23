/*
Graph Traversal - BFS
# Problem: 17863
# Memory: 2036KB
# Time: 0ms
*/
#include <iostream> 
#include <string.h>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

int N, M, T;
pair<int, int> sword;
int xy[4][2] = {{0, 1},{1, 0},{-1, 0},{0, -1}};
bool visit[101][101] = {false, };
queue<pair<int, int>> q;
int dist1 = 20000, dist2 = 20000;

void euclidean_dist(int x, int y, int cur_dist){
    dist2 = abs(N-1 - x) + abs(M-1 - y) + cur_dist;
}


int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    // input
    cin >> N >> M >> T;
    for(int i = 0; i < N; i++)
        for(int j = 0; j < M; j++){
            int a; cin >> a;
            if(a == 1) visit[i][j] = true;
            else if(a == 2) sword = make_pair(i, j);
        }

    q.push({0, 0});
    visit[0][0] = true;

    int dep = 0;
    while(!q.empty()){
        int q_size = q.size();
        for(int t = 0; t < q_size; t++){
            int x = q.front().first;
            int y = q.front().second;
            q.pop();
            if(x == sword.first && y == sword.second) euclidean_dist(x, y, dep);
            if(x == N-1 && y == M-1) {
                dist1 = dep;
                while(!q.empty()) q.pop();
                break;
            }

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

    int dist = min(dist1, dist2);
    if(dist <= T) cout << dist;
    else cout << "Fail";

    return 0;
}
