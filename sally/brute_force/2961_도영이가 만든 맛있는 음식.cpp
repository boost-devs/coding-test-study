/*
# Brute force
# Problem: 2961
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
vector<pair<int, int>> SB;
int result  = 1e9;

void dfs(int ind, int cur_s, int cur_b){
	int s = cur_s * SB[ind].first;
	int b = cur_b + SB[ind].second;
	result = min(result, abs(s-b));
	for(int i = ind + 1; i < N; i++)
		dfs(i, s, b);
}

int main(void) {
	cin.tie(NULL);
    ios::sync_with_stdio(false);

	cin >> N;
	for(int i = 0; i < N; i++){
		int a, b; cin >> a >> b;
		SB.push_back({a, b});
	}

	for(int i = 0; i < N; i++)
		dfs(i, 1, 0);

	cout << result << '\n';

	return 0;
}