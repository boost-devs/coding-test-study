/*
Graph Traversal - BFS
# Problem: 2636
# Memory: 2068KB
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

bool visit[101][101] = {false, };
int map[101][101] = {0, };
int xy[4][2] = {{0, 1},{1, 0},{-1, 0},{0, -1}};
int N, M; // 가로 세로
queue<pair<int, int> > q;
int cnt = 0;
int result = 0;

void init(){
    while(!q.empty()) q.pop();
    q.push({0, 0});
    for(int i = 0; i <N; i++)
        memset(visit[i], false, sizeof(visit[i]));
}

int BFS(){
    int cur_melt = 0;
    while(!q.empty()){
        pair<int, int> cur = q.front();
        q.pop();

        for(int i = 0; i< 4; i++){
            int x_ = cur.first + xy[i][0];
            int y_ = cur.second + xy[i][1];
            if(0 <= x_ && x_ < N && 0 <= y_ && y_< M){
                if(visit[x_][y_] == false){
                    if(map[x_][y_] == 0){
                        visit[x_][y_] = true;
                        q.push({x_, y_});
                    }else if(map[x_][y_] == 1){
                        visit[x_][y_] = true;
                        map[x_][y_] = 0;
                        cur_melt++;
                    }
                    
                }
            }
        }
    }
    return cur_melt;
}

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> N >> M;
    for(int i = 0; i <N; i++)
        for(int j = 0; j <M; j++)
            cin >> map[i][j];

    while(1){
        init();
        cnt++;
        int ret = BFS();
        if(ret == 0) break;
        else result = ret;
    }

    cout << cnt-1 << '\n' << result << '\n';

    return 0;
}
