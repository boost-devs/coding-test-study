/*
# Brute force
# Problem: 17144
# Memory: 2044KB
# Time: 296ms
*/
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <string>
#include <queue>
using namespace std;

int R, C, T;
int arr[51][51] = {0, }, tmp[51][51] = {0, };
int xy[4][2] = {{0, 1},{0, -1},{1, 0},{-1, 0}};
int air[2] = {-1, -1};
queue<pair<int, int>> q;

void spread_bad_air(){
	for(int i = 0; i < R; i++)
		memset(tmp[i], 0, sizeof(tmp[i]));

	for(int i = 0; i < R; i++)
		for(int j = 0; j < C; j++){
			vector<pair<int, int>> v;
			for(int k = 0; k < 4; k++){
				int x = i + xy[k][0];
				int y = j + xy[k][1];
				if(x < 0 || R <= x || y < 0 || C <= y) continue;
				if(arr[x][y] == -1) continue;
				v.push_back({x, y});
				// cout << "check: " << i << ' ' << j << ' ' << x << ' ' << y  << '\n';
			}
			int v_size = v.size();
			int spread_quant = arr[i][j] / 5;
			for(auto k : v)
				tmp[k.first][k.second] += spread_quant;
			tmp[i][j] += (arr[i][j] - (spread_quant * v_size));
		}
	tmp[air[0]][0] = tmp[air[1]][0] = -1;
	for(int i = 0; i < R; i++)
		for(int j = 0; j < C; j++) arr[i][j] = tmp[i][j];
}

void run_air_conditioner(){
	int upx = air[0];
	for(int i = upx; i > 0; i--) arr[i][0] = arr[i-1][0];
	for(int i = 0; i < C-1; i++) arr[0][i] = arr[0][i+1];
	for(int i = 0; i < upx; i++) arr[i][C-1] = arr[i+1][C-1];
	for(int i = C-1; i > 0; i--) arr[upx][i] = arr[upx][i-1];

	int downx = air[1];
	for(int i = downx+1; i < R; i++) arr[i-1][0] = arr[i][0];
	for(int i = 0; i < C-1; i++) arr[R-1][i] = arr[R-1][i+1];
	for(int i = R-1; i > downx; i--) arr[i][C-1] = arr[i-1][C-1];
	for(int i = C-1; i > 0; i--) arr[downx][i] = arr[downx][i-1];

	arr[upx][1] = arr[downx][1] = 0;
	arr[upx][0] = arr[downx][0] = -1;
}

void test(){
	cout << "==========" << '\n';
	for(int i = 0; i < R; i++){
		for(int j = 0; j < C; j++)
			cout << arr[i][j] << ' ';
		cout << '\n';
	}
}

int main(void){
	cin.tie(NULL);
    ios::sync_with_stdio(false);

	cin >> R >> C >> T;
	for(int i = 0; i < R; i++)
		for(int j = 0; j < C; j++){
			cin >> arr[i][j];
			if(arr[i][j] == -1){
				if(air[0] == -1) air[0] = i;
				else air[1] = i;
			}
				
		}
		
	while(T--){
		spread_bad_air();
		// test();
		run_air_conditioner();
		// test();
	}

	int result = 0;
	for(int i = 0; i < R; i++)
		for(int j = 0; j < C; j++)
			if(arr[i][j] != -1) result += arr[i][j];

	cout << result << '\n';

	return 0;
}