#include <string>
#include <vector>
#include <iostream>
#include <cmath>
#include <queue>
using namespace std;

vector<int> solution(int rows, int columns, vector<vector<int>> queries) {
    vector<int> answer;
    
    // init
    int arr[101][101] = {0,};
    int k = 0;
    for(int i = 0; i < rows; i++)
        for(int j = 0; j < columns; j++)
            arr[i][j] = ++k;

    int dir[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

    // roll
    int T = queries.size();
    for(int t = 0; t < T; t++){
        int x1 = queries[t][0]-1;
        int y1 = queries[t][1]-1;
        int x2 = queries[t][2]-1;
        int y2 = queries[t][3]-1;
        
        queue<pair<int, int>> loc;
        queue<int> val;
        
        vector<int> cnt;
        cnt.push_back(y2-y1);
        cnt.push_back(x2-x1);
        cnt.push_back(y2-y1);
        cnt.push_back(x2-x1);
        
        int cur_x = x1;
        int cur_y = y1;
        int d = 0;
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < cnt[i]; j++){
                loc.push({cur_x, cur_y});
                val.push(arr[cur_x][cur_y]);
                cur_x += dir[d][0];
                cur_y += dir[d][1];
            }
            d++;
        }
        
        pair<int, int> tmp = loc.front();
        loc.pop();
        loc.push(tmp);
        
        int min_val = 1000001;
        while(!loc.empty()){
            arr[loc.front().first][loc.front().second] = val.front();
            min_val = min(min_val, val.front());
            loc.pop();
            val.pop();
        }
        answer.push_back(min_val);
    }
    
    return answer;
}