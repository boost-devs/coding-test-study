/*
# Implementation
# Problem: 1913
# Memory: 5928KB
# Time: 108ms
*/
#include <iostream>
using namespace std;

int N, M;
int arr[1000][1000] = {0,};
int ret_x, ret_y;
int xy[4][2] = {{1, 0},{0, 1},{-1, 0},{0, -1},};
int x = 0, y = 0;
int cur_dir = 0;

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> N >> M;
    
    int T = N * N + 1;
    while(T--){
        arr[x][y] = T;

        int x_ = x + xy[cur_dir][0];
        int y_ = y + xy[cur_dir][1];

        if (T == 1) break;
        else if(T == M) {
            ret_x = x+1;
            ret_y = y+1;
        }

        if (0 > x_ || x_ >= N || 0 > y_ || y_ >= N || arr[x_][y_] != 0)
        {
            cur_dir = (cur_dir + 1) % 4;
            x_ = x + xy[cur_dir][0];
            y_ = y + xy[cur_dir][1];
        }
        
        x = x_;
        y = y_;
    }

    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++) cout << arr[i][j] << ' ';
        cout << '\n';
    }
    cout << ret_x << ' ' << ret_y;

    return 0;
}