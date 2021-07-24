/*
# Implementation
# Problem: 2615
# Memory: 2028KB
# Time: 0ms
*/
#include <iostream>
#include <vector>
#include <string>
#include <string.h>
#include <queue>
#include <cmath>
#include <algorithm>
using namespace std;

#define LEN 19

bool backup[3][20][20] = {false,};
bool arr[3][20][20] = {false,};
int dir[4][2] = {{-1, 1},{1, 0},{0, 1},{1, 1}}; // count direction
vector<pair<int, int>> v[3]; // start point
queue<pair<int, int>> q;
int winner = 0;

void init(int turn){
	for(int i = 0; i < LEN; i++)
		for(int j = 0; j < LEN; j++)
			arr[turn][i][j] = backup[turn][i][j];
}

bool right_up(int turn){
	if(v[turn].size() == 0) return false;
	for(int i = v[turn].size()-1; i >= 0; i--){
		int x = v[turn][i].first;
		int y = v[turn][i].second;
		if(arr[turn][x][y] == true){
			int x_ = x;
			int y_ = y;
			arr[turn][x_][y_] = false;
			int j = 1;
			for (j = 1; j <= 2 * LEN; j++) {
				x_ = x_ + dir[0][0];
				y_ = y_ + dir[0][1];
				if (0 <= x_ && x_ < LEN && 0 <= y_ && y_ < LEN && arr[turn][x_][y_])
					arr[turn][x_][y_] = false;
				else break;
			}
			if(j == 5){
				cout << turn << '\n' << x+1 << ' ' << y+1 << '\n';
				return true;
			}
		}
	}
	init(turn);
	return false;
}

bool right_down(int turn, int d){
	if(v[turn].size() == 0) return false;
	for(int i = 0; i < v[turn].size(); i++){
		int x = v[turn][i].first;
		int y = v[turn][i].second;
		if(arr[turn][x][y] == true){
			int x_ = x;
			int y_ = y;
			arr[turn][x_][y_] = false;
			int j = 1;
			for (j = 1; j <= 2 * LEN; j++) {
				x_ = x_ + dir[d][0];
				y_ = y_ + dir[d][1];
				if (0 <= x_ && x_ < LEN && 0 <= y_ && y_ < LEN && arr[turn][x_][y_])
					arr[turn][x_][y_] = false;
				else break;
			}
			if(j == 5){
				cout << turn << '\n' << x+1 << ' ' << y+1 << '\n';
				return true;
			}
		}
	}
	init(turn);
	return false;
}

int main(void) {
	cin.tie(NULL);
    ios::sync_with_stdio(false);

	int a;
	for(int i = 0; i < LEN; i++)
		for(int j = 0; j < LEN; j++){
			cin >> a;
			if(a != 0) {
				backup[a][i][j] = arr[a][i][j] = true;
				v[a].push_back({i, j});
			}
		}

	// right-up
	if (right_up(1)) return 0;
	if (right_up(2)) return 0;

	// others
	for(int i = 1; i < 4; i++){
		if(right_down(1, i)) return 0;
		if(right_down(2, i)) return 0;
	}

	cout << 0;

	return 0;
}