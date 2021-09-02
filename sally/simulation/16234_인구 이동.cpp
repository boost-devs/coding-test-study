/*
# Brute force
# Problem: 16234
# Memory: 2172KB
# Time: 172ms
*/
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <string>
#include <queue>
using namespace std;

int N, L, R;
int xy[4][2] = {{0, 1},{0, -1},{1, 0},{-1, 0}};
int arr[51][51] = {0, };
bool visit[51][51] = {false, };
int result = 0;
bool moved = false;
queue<pair<int, int>> q;
vector<pair<int, int>> v;

void init(){
	for(int i = 0; i < N; i++)
		memset(visit[i], false, sizeof(visit[i]));
	moved = false;
}

void BFS(int st_x, int st_y){
	while(!q.empty()) q.pop();
	v.clear();

	q.push({st_x, st_y});
	visit[st_x][st_y] = true;
	v.push_back({st_x, st_y});
	
	while(!q.empty()){
		int cur_x = q.front().first;
		int cur_y = q.front().second;
		q.pop();

		for(int i = 0; i < 4; i++){
			int x = cur_x + xy[i][0];
			int y = cur_y + xy[i][1];
			if(x < 0 || N <= x || y < 0 || N <= y || visit[x][y]) continue;
			int target = abs(arr[cur_x][cur_y] - arr[x][y]);
			if(target < L || R < target) continue;
			moved = visit[x][y] = true;
			v.push_back({x, y});
			q.push({x, y});
		}		
	}

	int sum_all = 0;
	int nums = v.size();
	for(auto i : v) sum_all += arr[i.first][i.second];
	int avg_all = sum_all / nums;
	for(auto i : v) arr[i.first][i.second] = avg_all;
}

int main(void){
	cin.tie(NULL);
    ios::sync_with_stdio(false);

	cin >> N >> L >> R;
	for(int i = 0; i < N; i++)
		for(int j = 0; j < N; j++)
			cin >> arr[i][j];

	
	while(1){
		init();
		for(int i = 0; i < N; i++)
			for(int j = 0; j < N; j++)
				if(!visit[i][j]) BFS(i, j);
		if(!moved) break;
		result++;
	}

	cout << result << '\n';

	return 0;
}