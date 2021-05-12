/*
Graph Traversal - BFS
# Problem: 2667
# Memory: 2164KB
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

int N;
int map[26][26] = {false,};
int xy[4][2] = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
queue<pair<int, int>> q;
vector<int> result;
vector<pair<int, int>> start_v;
string s;

int BFS(pair<int, int> st){
    int ret = 0;
    q.push(st);
    map[st.first][st.second] = false;

    while (!q.empty()){
        pair<int, int> cur = q.front();
        q.pop();
        ret++;

        for (int i = 0; i < 4; i++){
            int x_ = cur.first + xy[i][0];
            int y_ = cur.second + xy[i][1];
            if (0 <= x_ && x_ < N && 0 <= y_ && y_ < N){
                if (map[x_][y_] == true){
                    map[x_][y_] = false;
                    q.push({x_, y_});
                }
            }
        }
    }

    return ret;
}

int main(void)
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> N;
    for (int i = 0; i < N; i++){
        cin >> s;
        for (int j = 0; j < N; j++)
            if (s[j] == '1'){
                map[i][j] = true;
                start_v.push_back({i, j});
            }
    }

    for (auto sv : start_v)
        if (map[sv.first][sv.second] == true)
            result.push_back(BFS(sv));
 
    sort(result.begin(), result.end());
    cout << result.size() << '\n';
    for (auto i : result)
        cout << i << '\n';

    return 0;
}