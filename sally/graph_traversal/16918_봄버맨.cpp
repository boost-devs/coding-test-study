/*
Graph Traversal - BFS
# Problem: 16918
# Memory: 2456KB
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

int R, C, N;
char map[201][201] = {'.', };
int xy[4][2] = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
queue<pair<int, int> > q;
string s;

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> R >>C >> N;
    for(int i = 0; i < R; i++){
        cin >> s;
        for(int j = 0; j < C; j++){
            map[i][j] = s[j];
            if (map[i][j] == 'O')
                q.push({i, j}); // 세로, 가로 // R, C
        }        
    }

    if(N==1){
        for(int i = 0; i < R; i++){
            for(int j = 0; j < C; j++)
                cout << map[i][j];
            cout << '\n';
        }
    }
    else if(N % 2 == 0){
        string st = "";
        for(int i = 0; i < C; i++) 
            st += 'O';
        for(int i = 0; i < R; i++)
            cout << st << '\n';
    } else if(N % 4 == 1){
        // first bomb
        for(int i = 0; i < R; i++)
            for(int j = 0; j < C; j++)
                map[i][j] = 'O';

        int q_size = q.size();
        for(int t = 0; t < q_size; t++){
            int x = q.front().first;
            int y = q.front().second;
            q.pop();
            map[x][y] = '.';

            for(int i = 0; i < 4; i++){
                int x_ = x + xy[i][0];
                int y_ = y + xy[i][1];
                if(0 <= x_ && x_ < R && 0 <= y_ && y_ < C){
                    map[x_][y_] = '.';
                }
            }
        }
        // re-init
        for(int i = 0; i < R; i++){
            for(int j = 0; j <C; j++){
                if(map[i][j] == 'O') q.push({i, j});
            }
        }
        // new
        for(int i = 0; i < R; i++)
            for(int j = 0; j < C; j++)
                map[i][j] = 'O';

        q_size = q.size();
        for(int t = 0; t < q_size; t++){
            int x = q.front().first;
            int y = q.front().second;
            q.pop();
            map[x][y] = '.';

            for(int i = 0; i < 4; i++){
                int x_ = x + xy[i][0];
                int y_ = y + xy[i][1];
                if(0 <= x_ && x_ < R && 0 <= y_ && y_ < C){
                    map[x_][y_] = '.';
                }
            }
        }
        // print
        for(int i = 0; i < R; i++){
            for(int j = 0; j < C; j++){
                cout << map[i][j];
            }
            cout << '\n';
        }
        
    } else if(N % 4 == 3){
        for(int i = 0; i < R; i++)
            for(int j = 0; j < C; j++)
                map[i][j] = 'O';

        int q_size = q.size();
        for(int t = 0; t < q_size; t++){
            int x = q.front().first;
            int y = q.front().second;
            q.pop();
            map[x][y] = '.';

            for(int i = 0; i < 4; i++){
                int x_ = x + xy[i][0];
                int y_ = y + xy[i][1];
                if(0 <= x_ && x_ < R && 0 <= y_ && y_ < C){
                    map[x_][y_] = '.';
                }
            }
        }

        for(int i = 0; i < R; i++){
            for(int j = 0; j < C; j++){
                cout << map[i][j];
            }
            cout << '\n';
        }
    }

    return 0;
}