/*
# Implementation
# Problem: 4396
# Memory: 2024KB
# Time: 0ms
*/
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int N;
string str;
int arr[10][10] = {0, };
char output[10][10] = {' ', };
bool bomb = false;
int xy[8][2] = {{0, 1},{1, 0},{1, 1},{-1, 0},{0, -1},{-1, -1},{1, -1},{-1, 1}};
vector<pair<int, int>> v;

int main(void) {
	cin.tie(NULL);
    ios::sync_with_stdio(false);

	// init
	cin >> N;
	for(int i = 0; i < N; i++) {
		cin >> str;
		for(int j = 0; j < N; j++)
			if(str[j] == '*') {
				arr[i][j] = -1;
				v.push_back({i, j});
			}
	}

	// pre-process
	for(auto target : v)
		for(int i = 0; i < 8; i++){
			int new_x = target.first + xy[i][0];
			int new_y = target.second + xy[i][1];
			if (0 <= new_x && new_x < N && 0 <= new_y && new_y < N)
				if(arr[new_x][new_y] != -1)
					arr[new_x][new_y]++;
		}
			

	// make output
	for(int i = 0; i < N; i++) {
		cin >> str;
		for(int j = 0; j < N; j++)
			if(str[j] == 'x')
				if(arr[i][j] == -1) bomb = true;
				else output[i][j] = char(arr[i][j] + '0');
			else output[i][j] = '.';
	}

	// print output
	if(bomb)
		for(auto target : v) output[target.first][target.second] = '*';
		
	for(int i = 0; i < N; i++){
		for(int j = 0; j < N; j++) cout << output[i][j];
		cout << '\n';
	}


	return 0;
}