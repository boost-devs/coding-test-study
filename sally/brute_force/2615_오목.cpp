/*
# Brute force
# Problem: 2615
# Memory: 2024KB
# Time: 0ms
*/
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <string>
#include <queue>
#include <set>
using namespace std;

#define MAX 19

bool visited[4][MAX][MAX] = {false,};
int arr[MAX][MAX] = {0,};
int next_loc[4][2] = {{1, 0},{0, 1},{1, 1}, {-1, 1}};
int winner =  0;
int st_x, st_y;

void dfs(int cur_x, int cur_y, int dep, int dir){
	visited[dir][cur_x][cur_y] = true;
	int next_x = cur_x + next_loc[dir][0];
	int next_y = cur_y + next_loc[dir][1];
	if (0 <= next_x && next_x < MAX && 0 <= next_y && next_y < MAX // range check
		&& arr[cur_x][cur_y] == arr[next_x][next_y]) // color check
		dfs(next_x, next_y, dep + 1, dir);
	else
		if(dep == 5) winner = arr[cur_x][cur_y];
}

int main(void) {
	cin.tie(NULL);
    ios::sync_with_stdio(false);
	
	for(int i = 0; i < MAX; i++)
		for(int j = 0; j < MAX; j++)
			cin >> arr[i][j];
	
	// right,down
	for(int t = 0; t < 3; t++){
		for(int i = 0; i < MAX; i++){
			for(int j = 0; j < MAX; j++){
				if (!visited[t][i][j] && arr[i][j] != 0){
					dfs(i, j, 1, t);
					if (winner != 0){
						st_x = i;
						st_y = j;
						break;
					}
				}
			}
			if(winner!=0) break;
		}
		if(winner!=0) break;
	}

	// right, up
	if(winner == 0)
		for(int i = MAX - 1; i >= 0; i--){
			for(int j = 0; j < MAX; j++){
				if (!visited[3][i][j] && arr[i][j] != 0){
					dfs(i, j, 1, 3);
					if (winner != 0){
						st_x = i;
						st_y = j;
						break;
					}
				}
			}
			if(winner!=0) break;
		}

	cout << winner << '\n';
	if(winner != 0) cout << st_x + 1 << ' ' << st_y + 1;

	return 0;
}