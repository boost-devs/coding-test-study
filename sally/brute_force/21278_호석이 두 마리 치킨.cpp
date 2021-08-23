/*
# Brute force
# Problem: 21278
# Memory: 2164KB
# Time: 52ms
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
vector<bool> selector;
vector<int> con[101];
int result = 1e9;
vector<int> ans;

int all_visited(vector<int> visited){
	int ret = 2;
	for(int i = 1; i <= N; i++) {
		if(visited[i] == 0) return -1;
		ret += visited[i];
		if(ret > result) return result+1;
	}
	return ret;
}

int min_dist(vector<int> param){
	int a = param[0];
	int b = param[1];
	vector<int> visited(N+1, 0);
	queue<pair<int, int>> q;
	q.push({a, 0});
	q.push({b, 0});
	visited[a] = visited[b] = -1;
	int ret = 0;
	while(!q.empty()){
		int cur_node = q.front().first;
		int cur_sum = q.front().second;
		q.pop();
		for(auto cn: con[cur_node]){
			if(visited[cn] == 0){
				q.push({cn, cur_sum + 1});
				visited[cn] = cur_sum + 1;
			}
		}
		ret = all_visited(visited);
		if (ret != -1)
			return ret;
	}
	return ret;
}


int main(void){
	cin.tie(NULL);
    ios::sync_with_stdio(false);

	cin >> N >> M;
	for(int i = 0; i < M; i++){
		int a, b; cin >> a >> b;
		con[a].push_back(b);
		con[b].push_back(a);
	}
	for(int i = 0; i < N; i++)
		selector.push_back(false);
	selector[0] = selector[1] = true;
	int sel_len = selector.size();
	ans.push_back(0); ans.push_back(0);

	do{
		vector<int> tmp_v;	
		for(int i = 0; i < sel_len; i++)
			if(selector[i]) tmp_v.push_back(i+1);
		int target = min_dist(tmp_v);
		if(target < result){
			result = target;
			ans[0] = tmp_v[0];
			ans[1] = tmp_v[1];
		}
	}while(prev_permutation(selector.begin(), selector.end()));
	
	sort(ans.begin(), ans.end());
	cout << ans[0] << ' ' << ans[1] << ' ' << result * 2;

	return 0;
}