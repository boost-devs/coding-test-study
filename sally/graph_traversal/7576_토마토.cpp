/*
Graph Traversal - BFS
# Problem: 7576
# Memory: 7276KB
# Time: 80ms
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
bool map[1001][1001] = {false,}; // exist
int xy[4][3] = {{0, 1, 0}, {1, 0, 0}, {-1, 0, 0}, {0, -1, 0}};
queue<pair<int, int>> q;
int total = 0;

pair<int, int> BFS() {
    int ret = 0; 
    int dep = 0;
    while (!q.empty()){
        int q_size = q.size();
        dep++;
        for(int i = 0; i < q_size; i++){
            pair<int, int> cur = q.front();
            q.pop();
            ret++;

            for (int i = 0; i < 4; i++) {
                int x_ = cur.first + xy[i][0];
                int y_ = cur.second + xy[i][1];
                if (0 <= x_ && x_ < M && 0 <= y_ && y_ < N) {
                    if (map[x_][y_] == true) {
                        map[x_][y_] = false;
                        q.push({x_, y_});
                    }
                }
            }
        }
    }

    // cout << ret << ' ' << dep << '\n';
    return {ret, dep};
}

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> M >> N;
    for(int n = 0; n < N; n++){
        for(int m = 0; m < M; m++){
            int a;
            cin >> a;
            if(a == 1) q.push({m, n});
            else if(a == 0) map[m][n] = true;
            else total++;
        }
    }

    if(q.size() + total == (N*M)) cout << "0" << '\n';
    else{
        pair<int, int> rets = BFS();
        total += rets.first;
        if(total != (N*M)) cout << "-1" << '\n';
        else cout << rets.second - 1 << '\n';
    }

    return 0;
}