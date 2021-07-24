/*
# Implementation
# Problem: 16926
# Memory: 3592KB
# Time: 24ms
*/
#include <iostream>
#include <vector>
#include <string>
#include <string.h>
#include <queue>
#include <cmath>
#include <algorithm>
using namespace std;

int N, M, R;
bool visit[301][301] = {false, };
int arr[301][301] = {0, };
int result[301][301] = {0,};
int dir[4][2] = {{1, 0},{0, 1},{-1, 0},{0, -1}};
vector<vector<pair<int, int>>> v;

int main(void) {
	cin.tie(NULL);
    ios::sync_with_stdio(false);

	// input
	cin >> N >> M >> R;
	for(int i = 1; i <= N; i++)
		for(int j = 1; j <= M; j++)
			cin >> arr[i][j];
	
	// make belt
	int belt_num = min(N, M) / 2;
	for(int t = 1; t <= belt_num; t++){
		vector<pair<int, int>> tmp;
		int x = t;
		int y = t;
		visit[x][y] = true;
		tmp.push_back({x, y});
		int d = 0;
		while(1){
			int x_ = x + dir[d][0];
			int y_ = y + dir[d][1];
			if(x_ == t && y_ == t) break;
			if(1<= x_ && x_ <= N && 1<= y_ && y_ <= M && !visit[x_][y_]){
				tmp.push_back({x_, y_});
				visit[x_][y_] = true;
				x = x_;
				y = y_;
			} else d = (d + 1) % 4;
		}
		v.push_back(tmp);
	}

    // make answer
	for(auto target: v){
		int t_len = target.size();
		for(int i = 0; i <t_len; i++){
			int x = target[i].first;
			int y = target[i].second;
			int t = (i + R) % t_len;
			int x_ = target[t].first;
			int y_ = target[t].second;
			result[x_][y_] = arr[x][y];
		}
	}

	for(int i = 1; i <= N; i++){
		for(int j= 1; j <= M; j++)
		cout << result[i][j] << ' ';
		cout << '\n';
	}
	

	return 0;
}