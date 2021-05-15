/*
Graph Traversal - BFS
# Problem: 5547
# Memory: 2036KB
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

int W, H;
bool map[103][103] = {
    false,
}; // H, W
bool visit[103][103] = {
    false,
};
int xy_o[6][2] = {{-1, -1}, {0, -1}, {1, -1}, {1, 0}, {0, 1}, {-1, 0}}; // 열간이동, 행간이동 // 홀수
int xy_e[6][2] = {{-1, 0}, {0, -1}, {1, 0}, {1, 1}, {0, 1}, {-1, 1}};   // 열간이동, 행간이동 // 짝수
queue<pair<int, int>> q;
string s;
int result = 0;

int main(void)
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> W >> H;
    for (int i = 1; i <= H; i++)
        for (int j = 1; j <= W; j++)
        {
            int a;
            cin >> a;
            if (a == 1)
                map[i][j] = true;
        }

    q.push({0, 0});
    visit[0][0] = true;

    while (!q.empty())
    {
        pair<int, int> cur = q.front();
        q.pop();

        for (int i = 0; i < 6; i++)
        {
            int x_, y_;
            if (cur.first % 2 == 1)
            {
                x_ = cur.first + xy_e[i][0];
                y_ = cur.second + xy_e[i][1];
            }
            else
            {
                x_ = cur.first + xy_o[i][0];
                y_ = cur.second + xy_o[i][1];
            }
            if (0 <= x_ && x_ < H + 2 && 0 <= y_ && y_ < W + 2)
                if (map[x_][y_] == true)
                    result++;
        }

        for (int i = 0; i < 6; i++)
        {
            int x_, y_;
            if (cur.first % 2 == 1)
            {
                x_ = cur.first + xy_e[i][0];
                y_ = cur.second + xy_e[i][1];
            }
            else
            {
                x_ = cur.first + xy_o[i][0];
                y_ = cur.second + xy_o[i][1];
            }

            if (0 <= x_ && x_ < H + 2 && 0 <= y_ && y_ < W + 2)
            {
                if (visit[x_][y_] == false && map[x_][y_] == false)
                {
                    visit[x_][y_] = true;
                    q.push({x_, y_});
                }
            }
        }
    }

    cout << result << '\n';

    return 0;
}