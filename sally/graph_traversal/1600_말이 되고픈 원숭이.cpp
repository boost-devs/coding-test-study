/*
Graph Traversal - BFS
# Problem: 1600
# Memory: 3536KB
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

int K, N, M;
int common_move[4][2] = {{0, 1},{1, 0},{-1, 0},{0, -1}};
int horse_move[8][2] = {{2, 1},{1, 2},{-2, -1},{-1, -2},{-1, 2},{2, -1},{-2, 1},{1, -2}};
int map[201][201] = {0,};
bool visit[201][201][31] = {false, };
queue<pair<pair<int, int>, pair<int, int>>> q; // x, y, hop, chance
int result = -1;

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    // input
    cin >> K >> M >> N;
    for(int i = 0; i < N; i++)
        for(int j = 0; j < M; j++){
            cin >> map[i][j];
        }

    q.push({{0, 0}, {0, 0}}); // used chance: 0
    visit[0][0][0] = true;

    int dep = 0;
    while(!q.empty()){
        int q_size = q.size();
        for(int t = 0; t < q_size; t++){
            int x = q.front().first.first;
            int y = q.front().first.second;
            int hop = q.front().second.first; // hop num
            int chance = q.front().second.second; // used chance
            q.pop();

            if(x == N-1 && y == M-1) {
                result = dep;
                while(!q.empty()) q.pop();
                break;
            }

            for(int i = 0; i < 4; i++){
                int x_ = x + common_move[i][0];
                int y_ = y + common_move[i][1];
                if (0 <= x_ && x_ < N && 0 <= y_ && y_ < M)
                    if(map[x_][y_] == 0 && visit[x_][y_][chance] == false){
                        q.push({{x_, y_}, {hop+1, chance}});
                        visit[x_][y_][chance] = true;
                    }
            }
            
            if(chance < K)
                for(int i = 0; i < 8; i++){
                    int x_ = x + horse_move[i][0];
                    int y_ = y + horse_move[i][1];
                    if (0 <= x_ && x_ < N && 0 <= y_ && y_ < M)
                        if(map[x_][y_] == 0 && visit[x_][y_][chance+1] == false){
                            q.push({{x_, y_}, {hop + 1, chance + 1}});
                            visit[x_][y_][chance+1] = true;
                        }
                }
        }
        dep++;
    }

    cout << result;

    return 0;
}
