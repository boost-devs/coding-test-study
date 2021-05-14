/*
Graph Traversal - BFS
# Problem: 7569
# Memory: 4616KB
# Time: 104ms
*/
#include <iostream>
#include <string.h>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

int N, M, H;
bool map[101][101][101] = {false,}; // exist
int xy[6][3] = {{0, 1, 0}, {1, 0, 0}, {-1, 0, 0}, {0, -1, 0}, {0, 0, 1}, {0, 0, -1}}; // x, y, z
queue<pair<pair<int, int>, int>> q;
int total = 0;

pair<int, int> BFS() {
    int ret = 0; 
    int dep = 0;
    while (!q.empty()){
        int q_size = q.size();
        dep++;
        for(int i = 0; i < q_size; i++){
            pair<pair<int, int>, int> cur = q.front();
            q.pop();
            ret++;

            for (int i = 0; i < 6; i++) {
                int x_ = cur.first.first + xy[i][0];
                int y_ = cur.first.second + xy[i][1];
                int z_ = cur.second + xy[i][2];
                if (0 <= x_ && x_ < M && 0 <= y_ && y_ < N && 0 <= z_ && z_ < H) {
                    if (map[x_][y_][z_] == true) {
                        map[x_][y_][z_] = false;
                        q.push({{x_, y_}, z_});
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

    cin >> M >> N >> H;
    for(int h = 0; h < H; h++){
        for(int n = 0; n < N; n++){
            for(int m = 0; m < M; m++){
                int a;
                cin >> a;
                if(a == 1) q.push({{m, n}, h});
                else if(a == 0) map[m][n][h] = true;
                else total++;
            }
        }
    }

    if(q.size() + total == (N*M*H)) cout << "0" << '\n';
    else{
        pair<int, int> rets = BFS();
        total += rets.first;
        if(total != (N*M*H)) cout << "-1" << '\n';
        else cout << rets.second - 1 << '\n';
    }

    return 0;
}