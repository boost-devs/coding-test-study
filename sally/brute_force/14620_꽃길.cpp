/*
# Brute force
# Problem: 14620
# Memory: 2020KB
# Time: 0ms
*/
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <string>
using namespace std;

int N;
int result = 1e9;
int to_buy[5][2] = {{0,0},{0,1},{1,0},{-1,0},{0,-1}};
int price[11][11] = {0,};

void DFS(int cur_x, int cur_y, int dep, int total, bool arr1[11][11]){
	bool arr2[11][11] = {false,};
	for(int i = 0; i < 11; i++)
		for(int j = 0; j < 11; j++)
			arr2[i][j] = arr1[i][j];
			
	for(int i = 0; i < 5; i++){
		int x = cur_x + to_buy[i][0];
		int y = cur_y + to_buy[i][1];
		if(arr2[x][y]) return;
		arr2[x][y] = true;
		total += price[x][y];
	}
	if(dep == 3) result = min(result, total);
	else
		for(int i = cur_x; i < N-1; i++)
			for(int j = 1; j < N-1; j++){
				if(i == cur_x && j <= cur_y) continue;
				else DFS(i, j, dep+1, total, arr2);
			}
}

int main(void) {
	cin.tie(NULL);
    ios::sync_with_stdio(false);

	cin >> N;
	for(int i = 0; i < N; i++)
		for(int j = 0; j < N; j++)
			cin >> price[i][j];

	bool arr[11][11] = {false,};
	for(int i = 1; i < N-1; i++)
		for(int j = 1; j < N-1; j++)
			DFS(i, j, 1, 0, arr);

	cout << result;

	return 0;
}