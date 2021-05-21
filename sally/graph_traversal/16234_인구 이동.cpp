/*
Graph Traversal - DFS, BFS
# Problem: 16234
# Memory: 2180KB
# Time: 240ms
*/
#include <iostream> 
#include <string.h>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

bool visit[51][51] = {false, };
int map[51][51] = {0, };
int map_save[51][51] = {0, };
int xy[4][2] = {{0, 1},{1, 0},{-1, 0},{0, -1}};
int N, L, R;
queue<pair<int, int> > q;
int result = 0;



void BFS(pair<int, int> start_v){
    vector<pair<int, int>> v;
    v.push_back(start_v);
    q.push(start_v);
    visit[start_v.first][start_v.second] = true;

    while(!q.empty()){
        pair<int, int> cur = q.front();
        q.pop();

        for(int i = 0; i< 4; i++){
            int x_ = cur.first + xy[i][0];
            int y_ = cur.second + xy[i][1];
            if(0 <= x_ && x_ < N && 0 <= y_ && y_< N){
                if(visit[x_][y_] == false){
                    int det = abs(map[x_][y_] - map[cur.first][cur.second]);
                    if(L <= det && det <= R){
                        visit[x_][y_] = true;
                        v.push_back({x_,y_});
                        q.push({x_, y_});
                    }
                }
            }
        }
    }
    
    int avg = 0;
    int v_size = v.size();
    for(int i = 0; i <v_size; i++)
        avg += map[v[i].first][v[i].second];
    for (int i = 0; i < v_size; i++)
        map_save[v[i].first][v[i].second] = (avg/v_size);
}

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    // init
    cin >> N >> L >> R;
    for(int i = 0; i < N; i++)
        for(int j = 0; j< N; j++)
            cin >> map[i][j];

    while(1){
        // init
        for(int i = 0; i < N; i++)
            memset(visit[i], false, sizeof(visit[i]));

        // Do?
        bool flag = false;
        for(int i = 0; i < N; i++){
            for(int j = 0; j< N; j++){
                for(int k = 0; k < 2; k++){
                    int i_ = i + xy[k][0];
                    int j_ = j + xy[k][1];
                    if(0<=i_ && i_<N && 0<=j_ && j_<N){
                        int de = abs(map[i][j] - map[i_][j_]);
                        if(L<=de && de<=R){
                            flag = true;
                            break;
                        }
                    }
                }
                if(flag == true) break;
            }
            if(flag == true) break;
        }
        if(flag == false) break;

        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                if(visit[i][j] == false){
                    BFS({i, j});
                    // DFS({i, j}, map[i][j], 1);
                }
            }
        }

        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                if(map_save[i][j] != 0){
                    map[i][j] = map_save[i][j];
                    map_save[i][j] = 0;
                }
            }
        }

        result++;
    }

    cout << result << '\n';

    return 0;
}
