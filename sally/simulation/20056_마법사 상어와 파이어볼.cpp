/*
# Simulation
# Problem: 20056
# Memory: 3372KB
# Time: 24ms
*/
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <string>
#include <queue>
using namespace std;

int N, M, K;
vector<pair<pair<int, int>, pair<int, pair<int, int>>>> v; // {{x, y} , {질량, {방향, 속력}}}
vector<int> arr[51][51];
int dir[8][2] = {{-1, 0},{-1, 1},{0, 1},{1, 1},{1, 0},{1, -1},{0, -1},{-1, -1}};
int new_dir[2][4] = {{0, 2, 4, 6}, {1, 3, 5, 7}};

void move() {
	for(int i = 0; i < N; i++)
		for(int j = 0; j < N; j++)
			arr[i][j].clear();

	int cnt = 0;
	for(auto &target : v){
		int x = target.first.first;
		int y = target.first.second;
		int d = target.second.second.first;
		int s = target.second.second.second;
		int next_x = x + (s * dir[d][0]);
		int next_y = y + (s * dir[d][1]);
		next_x = (next_x + (N * 1000)) % N;
		next_y = (next_y + (N * 1000)) % N;

		target.first.first = next_x;
		target.first.second = next_y;
		arr[next_x][next_y].push_back(cnt);
		cnt++;
	}
}

int find_mass(int a, int b){
	int cnt = 0;
	for(auto i : arr[a][b])
		cnt += v[i].second.first;
	return (cnt / 5);
}

int find_speed(int a, int b){
	int cnt = 0;
	for(auto i : arr[a][b])
		cnt += v[i].second.second.second;
	return (cnt / arr[a][b].size());
}

int find_dir(int a, int b){
	int ret = 0;
	int arrsize = arr[a][b].size();
	v[arr[a][b][0]].first.first = -1;
	for(int i = 1; i < arrsize; i++){
		if ((v[arr[a][b][i - 1]].second.second.first % 2) != (v[arr[a][b][i]].second.second.first % 2)) ret = 1;
		v[arr[a][b][i]].first.first = -1;
	}
	return ret;
}

void sum_div(){
	vector<pair<pair<int, int>, pair<int, pair<int, int>>>> tmp;
	for(int i = 0; i < N; i++)
		for(int j = 0; j < N; j++){
			if(arr[i][j].size() >= 2){
				int ms = find_mass(i, j);
				if(ms == 0) continue;
				int ss = find_speed(i, j);
				int ds = find_dir(i, j);
				for(int k = 0; k < 4; k++)
                    tmp.push_back({{i, j}, {ms, {new_dir[ds][k], ss}}});
					
			} else if(arr[i][j].size() == 1) tmp.push_back(v[arr[i][j][0]]);
			
		}

	for(int i = 0; i < N; i++)
		for(int j = 0; j < N; j++)
			arr[i][j].clear();

	int cnt = 0;
	v.clear();
	for(auto i : tmp) {
		v.push_back(i);
		arr[i.first.first][i.first.second].push_back(cnt);
		cnt++;
	}
	
}

int main(void){
	cin.tie(NULL);
    ios::sync_with_stdio(false);

	cin >> N >> M >> K;
	for(int i = 0; i < M; i++){
		int a, b, c, d, e; cin >> a >> b >> c >> e >> d;
		a--; b--;
		arr[a][b].push_back(i);
		v.push_back({{a, b}, {c, {d, e}}});
	}

	while(K--){
		move();
		sum_div();
	}

	int result = 0;
	for(auto i : v) result += i.second.first;
	cout << result << '\n';
	
	return 0;
}