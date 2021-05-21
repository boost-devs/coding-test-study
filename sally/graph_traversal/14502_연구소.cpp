/*
Graph Traversal - BFS, next_permutation
# Problem: 14502
# Memory: 2020KB
# Time: 56ms
*/
#include <iostream> 
#include <string.h>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

bool visit[10][10] = {false, };
int map[10][10] = {0, };
int xy[4][2] = {{0, 1},{1, 0},{-1, 0},{0, -1}};
int N, M;
vector<bool> v;
vector<pair<int, int>> start_v;
vector<pair<int, int>> pth;
queue<pair<int, int>> q;
int result = 0;

int BFS(){
    int ret = 0;

    while(!q.empty()){
        pair<int, int> cur = q.front();
        q.pop();
        
        for(int i = 0; i < 4; i++){
            int x_ = cur.first + xy[i][0];
            int y_ = cur.second + xy[i][1];
            if(0<=x_ && x_<N && 0<=y_ && y_<M)
                if(visit[x_][y_] == false && map[x_][y_] != 1){
                    visit[x_][y_] = true;
                    q.push({x_, y_});
                    ret++;
                }
        }
    }

    return ret; // 새 감염
}

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> N >> M;
    for(int i = 0; i <N; i++){
        for(int j =0; j<M; j++){
            cin >> map[i][j];
            if(map[i][j] == 0) {
                v.push_back(false);
                pth.push_back({i, j});
            } else if(map[i][j] == 2) {
                start_v.push_back({i, j});
            }
        }
    }

    int s_size = start_v.size(); // 바이러스 수
    int v_size = v.size(); // 빈칸 수
    v[v_size-1] = v[v_size-2] = v[v_size-3] = true;

	do{
        // init
        for(int i = 0; i < 10; i++)
            memset(visit[i], false, sizeof(visit[i]));
        for(int i = 0; i < v_size; i++)
            if(v[i] == true) visit[pth[i].first][pth[i].second] = true;
        for(int i = 0; i < s_size; i++){
            q.push(start_v[i]);
            visit[start_v[i].first][start_v[i].second] = true;
        }

        int emp = v_size - 3 - BFS();
        result = max(result, emp);
	}while(next_permutation(v.begin(),v.end()));

    cout << result << '\n';

    return 0;
}
