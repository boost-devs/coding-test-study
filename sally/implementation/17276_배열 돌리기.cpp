/*
# Implementation
# Problem: 17267
# Memory: 4548KB
# Time: 232ms
*/
#include <iostream>
#include <vector>
#include <deque>
#include <cmath>
using namespace std;

int T, N, dir;
int arr[500][500] = {0,};
int result[500][500] = {0,};
int center;

deque<pair<int, int>> q[260];
deque<pair<int, int>> p[260];

void init(){
	// input
	cin >> N >> dir;
	for(int i = 0; i < N; i++)
		for(int j = 0; j < N; j++){
			cin >> arr[i][j];
			result[i][j] = arr[i][j];
		}
	
	// fill deque
	center = N / 2;
	for(int i = 0; i < center; i++)
		while(!q[i].empty()) {
			q[i].pop_back();
			p[i].pop_back();
		}
	for(int i = 0; i < center; i++){
		q[i].push_back({i, i});
		q[i].push_back({i, center});

		q[i].push_back({i, N-1-i});
		q[i].push_back({center, N-1-i});

		q[i].push_back({N-1-i, N-1-i});
		q[i].push_back({N-1-i, center});

		q[i].push_back({N-1-i, i});
		q[i].push_back({center, i});
		//
		p[i].push_back({i, i});
		p[i].push_back({i, center});

		p[i].push_back({i, N-1-i});
		p[i].push_back({center, N-1-i});

		p[i].push_back({N-1-i, N-1-i});
		p[i].push_back({N-1-i, center});

		p[i].push_back({N-1-i, i});
		p[i].push_back({center, i});
	}
}

void rotate(){
	bool right = true;  // >
	if(dir < 0) right = false; // <
	int num = abs(dir / 45);

	if(!right){
		for(int i = 0; i < center; i++)
			for(int j = 0; j < num; j++){
				q[i].push_front(q[i][q[i].size()-1]);
				q[i].pop_back();
			}
	} else{
		for(int i = 0; i < center; i++)
			for(int j = 0; j < num; j++){
				q[i].push_back(q[i][0]);
				q[i].pop_front();
			}
	}

	for(int i = 0; i < center; i++){
		for(int j = 0; j < 8; j++){
			int x = q[i].front().first;
			int y = q[i].front().second;
			q[i].pop_front();
			int target_x = p[i].front().first;
			int target_y = p[i].front().second;
			p[i].pop_front();
			result[x][y] = arr[target_x][target_y];
		}
	}
}

void printer(){
	for(int i = 0; i < N; i++){
		for(int j = 0; j < N; j++)
			cout << result[i][j] << ' ';
		cout << '\n';
	}
}

int main(void) {
	cin.tie(NULL);
    ios::sync_with_stdio(false);

	cin >> T;
	while(T--){
		init();
		rotate();
		printer();
	}

	return 0;
}
