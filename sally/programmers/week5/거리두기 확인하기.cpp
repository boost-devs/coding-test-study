#include <string>
#include <vector>
#include <queue>
#include <iostream>
using namespace std;

vector<int> solution(vector<vector<string>> places) {
    vector<int> answer;
    int N = 5;
    int dir[4][2] = {{0,1},{1,0},{0,-1},{-1,0}};
    bool visit[5][5] = {0,};
    
    int testcase = places.size();
    for(int T = 0; T < testcase; T++){
        // get targets
        vector<pair<int, int>> target;
        for(int i = 0; i < N; i++)
            for(int j = 0; j < N; j++)
                if(places[T][i][j] == 'P')
                    target.push_back({i, j});

        // check targets
        bool end_flag = false;
        int target_size = target.size();
        for(int t = 0; t < target_size; t++){
            // init
            for(int i = 0; i < N; i++)
                for(int j = 0; j < N; j++)
                    visit[i][j] = false;
            queue<pair<int, int>> q;
            int st_x = target[t].first;
            int st_y = target[t].second;
            q.push({st_x, st_y});
            visit[st_x][st_y] = true;
            
            // dep=2 search
            int cnt = 0;
            while(!q.empty()){
                int q_size = q.size();
                if(cnt == 2) break;
                cnt++;
                for(int k = 0; k < q_size; k++){
                    int x = q.front().first;
                    int y = q.front().second;
                    q.pop();

                    for(int i = 0; i < 4; i++){                    
                        int nex_x = x + dir[i][0];
                        int nex_y = y + dir[i][1];
                        if(nex_x < 0 || nex_x > 4 || nex_y < 0 || nex_y > 4) continue;
                        if(visit[nex_x][nex_y] || places[T][nex_x][nex_y] == 'X') continue;
                        if(places[T][nex_x][nex_y] == 'P') end_flag = true;
                        visit[nex_x][nex_y] = true;
                        q.push({nex_x, nex_y});

                        if(end_flag) break;   
                    }
                    if(end_flag) break;   
                }
                if(end_flag) break;   
            }
            if(end_flag) break;
        }
        if(end_flag) answer.push_back(0);
        else answer.push_back(1);
    }
    
    return answer;
}