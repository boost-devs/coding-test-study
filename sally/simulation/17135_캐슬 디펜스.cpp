/*
# Simulation
# Problem: 17135
# Memory: 2036KB
# Time: 4ms
*/
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <string>
#include <queue>
#include <stack>
#include <deque>
#include <set>
using namespace std;

int N, M, D;
int enemy = 0;
int arr[20][20] = {0,};
int origin[20][20] = {0,};
vector<bool> tf;
vector<int> cand;
int result = 0;
set<pair<int, int>> s;
vector<pair<int, pair<int, int>>> v[3];

void init(){
	for(int i = 0; i < N+1; i++)
		for(int j = 0; j < M+1; j++) arr[i][j] = origin[i][j];

	for(int i = 0; i < 3; i++){
		v[i].clear();
		for(int j = 0; j < N; j++)
			for(int k = 0; k < M; k++){
				int dist = abs(j - N) + abs(k - cand[i]);
				if (dist <= D) v[i].push_back({dist, {k, j}}); // 거리, ㅡ, ㅣ
			}
		sort(v[i].begin(), v[i].end());
	}
}

int shoot(){
	s.clear();
	for(int i = 0; i < 3; i++){
		for(auto target : v[i]){
			if(arr[target.second.second][target.second.first] == 1){
				s.insert({target.second.second, target.second.first});
				break;
			}
		}
	}

	int ret = s.size();
	for(auto i: s)
		arr[i.first][i.second] = 0;
	return ret;
}

int move(){
	int ret = 0;
	for(int i = 0; i < M; i++)
		if(arr[N-1][i] == 1) ret++;
	for(int i = N-1; i > 0; i--)
		for(int j = 0; j < M; j++){
			arr[i][j] = arr[i-1][j];
		}
	for(int i = 0; i < M; i++)
		arr[0][i] = 0;
	return ret;
}

int game(){
	int ret = 0;
	int gone = 0;
	init();
	while(1){
		if(ret + gone == enemy) break;
		ret += shoot();
		gone += move();
	}
	return ret;
}

int main(void) {
	cin.tie(NULL);
	ios::sync_with_stdio(false);

	cin >> N >> M >> D;
	for(int i = 0; i < N; i++)
		for(int j = 0; j < M; j++){
			cin >> origin[i][j];
			if(origin[i][j] == 1) enemy++;
			arr[i][j] = origin[i][j];
		}
			

	for(int i = 0; i < (M-3); i++) tf.push_back(false);
	for(int i = 0; i < 3; i++) tf.push_back(true);
	int cnt = 0;
	do{
		cand.clear();
		for(int i = 0; i < M; i++)
			if(tf[i]) cand.push_back(i);
		result = max(result, game());
	}while(next_permutation(tf.begin(), tf.end()));
	
	cout << result << '\n';

	return 0;
}