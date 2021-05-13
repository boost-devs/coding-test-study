/*
Graph Traversal - BFS
# Problem: 2178
# Memory: 2060KB
# Time: 0ms
*/
#include <iostream>
#include <string.h>
#include <vector>
#include <queue>
#include <string>
using namespace std;

int N, M;
int map[101][101] = {false,};
string s;
queue<pair<int, int>> q;
int result = 0;
int xy[4][2] = {{0, 1},{1, 0},{-1, 0},{0, -1}};

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >>N >>M;
    for(int i = 0; i < N; i++){
        cin >> s;
        for(int j = 0; j < M; j++)
            if(s[j] == '1') map[i][j] = true;
    }

    q.push({0, 0});
    map[0][0] = false;

    while(!q.empty()){
        int q_size = q.size();
        for(int t = 0; t < q_size; t++){
            pair<int, int> cur = q.front();
            q.pop();
            if(cur.first == N-1 && cur.second == M-1) {
                while(!q.empty()) q.pop();
                break;
            }
            for(int i = 0; i <4; i++){
                int x_ = cur.first + xy[i][0];
                int y_ = cur.second + xy[i][1];
                if(0 <= x_ && x_ < N && 0 <= y_ && y_ <M){
                    if(map[x_][y_] == true){
                        map[x_][y_] = false;
                        q.push({x_, y_});
                    }
                }
            }
        }
        result++;
    }
    
    cout <<result << '\n';


    return 0;
}