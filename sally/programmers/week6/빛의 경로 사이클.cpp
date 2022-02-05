#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

vector<int> solution(vector<string> grid) {
    vector<int> answer;
    int dir[4][2] = {{-1,0},{0,1},{1,0},{0,-1}};
    
    // init
    int N = grid.size();
    int M = grid[0].size();
    
    int visit[501][501][4] = {false,};
    int arr[501][501] = {0,};
    for(int i = 0; i < N; i++)
        for(int j = 0; j < M; j++){
            if(grid[i][j] == 'S') arr[i][j] = 0;
            else if(grid[i][j] == 'L') arr[i][j] = -1;
            else if(grid[i][j] == 'R') arr[i][j] = 1;
        }
    
    // check all cases
    for(int i = 0; i < N; i++)
        for(int j = 0; j < M; j++)
            for(int k = 0; k < 4; k++){ // light direction
                int cur_dir = k, cur_x = i, cur_y = j;
                int cnt = 0;
                if(visit[cur_x][cur_y][cur_dir]) continue;
                while(1){
                    if(visit[cur_x][cur_y][cur_dir]) break;
                    visit[cur_x][cur_y][cur_dir] = true;
                    cnt++;
                    
                    cur_x = (cur_x + dir[cur_dir][0] + N) % N;
                    cur_y = (cur_y + dir[cur_dir][1] + M) % M; 
                    
                    cur_dir = (cur_dir + arr[cur_x][cur_y] + 4) % 4;
                }
                answer.push_back(cnt);
            }
    
    sort(answer.begin(), answer.end());
    return answer;
}