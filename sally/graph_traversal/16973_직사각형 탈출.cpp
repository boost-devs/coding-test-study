/*
Graph Traversal - BFS
# Problem: 16973
# Memory: 3136KB
# Time: 76ms
*/
#include <iostream> 
#include <string.h>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

int N, M, H, W;
pair<int, int> start_v, end_v;
int xy[4][2] = {{0, 1},{1, 0},{-1, 0},{0, -1},};
bool visit[1001][1001] = {false, }; // true: can't go // false: can go
int result = -1;
queue<pair<int, int>> cant;
queue<pair<int, int>> q;

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    // input
    cin >> N >> M;
    for(int i = 0; i < N; i++)
        for(int j = 0; j < M; j++){
            int a; cin >> a;
            if(a == 1) {
                cant.push({i, j});
                visit[i][j] = true;
            }
        }
    cin >> H >> W >> start_v.first >> start_v.second >> end_v.first >> end_v.second;
    start_v.first--; start_v.second--;
    end_v.first--; end_v.second--;

    for(int i =0; i < N; i++)
        for (int j = M - W + 1; j < M; j++)
            visit[i][j] = true;

    for (int j = 0; j < M; j++)
        for (int i = N - H + 1; i < N; i++)
            visit[i][j] = true;

    // visit update
    while(!cant.empty()){
        int x = cant.front().first;
        int y = cant.front().second;
        cant.pop();

        for(int i = 0; i < H; i++){
            for(int j = 0; j < W; j++){
                int x_ = x - i;
                int y_ = y - j;
                if(0 <= x_ && 0 <= y_)
                    visit[x_][y_] = true;
            }
        }
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

            if(x == end_v.first && y == end_v.second) result = dep;

            for(int i = 0; i < 4; i++){
                int x_ = x + xy[i][0];
                int y_ = y + xy[i][1];
                if (0 <= x_ && x_ < N && 0 <= y_ && y_ < M)
                    if(visit[x_][y_] == false){
                        q.push({x_, y_});
                        visit[x_][y_] = true;}
            }
        }
        dep++;
    }

    cout << result << '\n';


    return 0;
}
