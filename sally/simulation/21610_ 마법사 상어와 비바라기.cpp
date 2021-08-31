/*
# Simulation
# Problem: 21610
# Memory: 2172KB
# Time: 4ms
*/
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <string>
#include <queue>
using namespace std;

int N, M;
int arr[51][51] = {0, };
int dir[9][2] = {{0, 0}, {0, -1},{-1, -1},{-1, 0},{-1, 1},{0, 1},{1, 1},{1, 0},{1, -1}};
int diag[4][2] = {{1, 1},{-1, 1},{-1, -1},{1, -1}};
bool visit[51][51] = {false, };
vector<pair<int, int>> cand, cmd;

void func(int d, int s){
	// init
	for(int i = 0; i < N; i++)
		for(int j = 0; j < N; j++)
			visit[i][j] = false;

	vector<pair<int, int>> new_cand;
	for(auto i : cand){
		// 1. 구름이 이동한다.
		int x = i.first;
		int y = i.second;
		int next_x = x + (s * dir[d][0]);
		int next_y = y + (s * dir[d][1]);
		next_x = (next_x + (N * 51)) % N;
		next_y = (next_y + (N * 51)) % N;

		arr[next_x][next_y]++; // 2. 비가 내린다.
		visit[next_x][next_y] = true; // 3. 구름 사라진다

		new_cand.push_back({next_x, next_y}); // 비 내린 곳 저장
	}

	// 4. 물복사버그 마법
	for(auto i : new_cand){
		int next_x = i.first;
		int next_y = i.second;
		int cnt = 0;
		for(int j = 0; j < 4; j++){
			int arx = next_x + diag[j][0];
			int ary = next_y + diag[j][1];
			if (0 <= arx && arx < N && 0 <= ary && ary < N && arr[arx][ary] != 0) cnt++;
		}
		arr[next_x][next_y] += cnt;
	}

	// 5. 비내리기, 구름 위치 선정
	cand.clear();
	for(int i = 0; i < N; i++)
		for(int j = 0; j < N; j++)
			if(arr[i][j] >= 2 && !visit[i][j]){
				arr[i][j] -= 2;
				cand.push_back({i, j});
			}	
}

int main(void){
	cin.tie(NULL);
    ios::sync_with_stdio(false);

	// input
	cin >> N >> M;
	for(int i = 0; i < N; i++)
		for(int j = 0; j < N; j++)
			cin >> arr[i][j];
	
	for(int i = 0; i < M; i++){
		int a, b; cin >> a >> b;
		cmd.push_back({a, b});
	}

	// init
	cand.push_back({N-1, 0});
	cand.push_back({N-1, 1});
	cand.push_back({N-2, 0});
	cand.push_back({N-2, 1});

	// call func
	for(auto T: cmd){
		int d = T.first;
		int s = T.second;
		func(d, s);
	}

	// count result
	int result = 0;
	for(int i = 0; i < N; i++)
		for(int j = 0; j < N; j++)
			result += arr[i][j];
	cout << result << '\n';
	
	return 0;
}