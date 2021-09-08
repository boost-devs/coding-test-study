/*
# Simulation
# Problem: 16236
# Memory: 2028KB
# Time: 0ms
*/
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <string>
#include <queue>
using namespace std;

int N;
int arr[21][21] = {0, };
bool visit[21][21] = {false, };
int xy[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
int cur_size = 2;
int cur_eaten = 0;
int result = 0;
queue<pair<int, int>> q;
pair<int, int> cur_loc;

int eat_fish(){
	while(!q.empty()) q.pop();
	int ret = 0;
	for(int i = 0; i < N; i++)
		for(int j = 0; j < N; j++)
			visit[i][j] = false;
	q.push(cur_loc);
	visit[cur_loc.first][cur_loc.second] = true;

	while(!q.empty()){
		vector<pair<int, int>> cand;
		int q_size = q.size();
		ret++;
		for(int t = 0; t < q_size; t++){
			int cur_x = q.front().first;
			int cur_y = q.front().second;
			q.pop();
			for(int i = 0; i < 4; i++){
				int x = cur_x + xy[i][0];
				int y = cur_y + xy[i][1];
				if(x < 0 || N <= x || y < 0 || N <= y || visit[x][y] || arr[x][y] > cur_size) continue;
				if(arr[x][y] < cur_size && arr[x][y] != 0) cand.push_back({x, y});
				visit[x][y] = true;
				q.push({x, y});
				
			}
		}
		if(cand.size()!=0){
			sort(cand.begin(), cand.end());
			int x = cand[0].first;
			int y = cand[0].second;
			arr[x][y] = 0;
			cur_loc = make_pair(x, y);
			cur_eaten++;
			if(cur_eaten == cur_size) {
				cur_size++;
				cur_eaten = 0;
			}
			return ret;
		}
	}
	
	return -1;
}

int main(void){
	cin.tie(NULL);
    ios::sync_with_stdio(false);

	cin >> N;
	for(int i = 0 ; i < N; i++)
		for(int j = 0; j < N; j++){
			cin >> arr[i][j];
			if(arr[i][j] == 9) {
				cur_loc = make_pair(i, j);
				arr[i][j] = 0;
			}
		}
	
	while(1){
		int ret = eat_fish();
		if (ret == -1) break;
		else result += ret;
	}

	cout << result;


	return 0;
}