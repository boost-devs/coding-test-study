/*
# Simulation
# Problem: 17140
# Memory: 2376KB
# Time: 0ms
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

int r, c, k;
int r_cnt = 3, c_cnt = 3;
int arr[300][300] = {0, };
int num[101] = {0, };

vector<pair<int, int>> v;
int result = 0;

void init() {
	for (int i = 0; i < 101; i++) num[i] = 0;
	v.clear();
}

void cal_R() {
	int max_c = 0;
	for (int i = 0; i < r_cnt; i++) {
		init();
		for (int j = 0; j < c_cnt; j++) num[arr[i][j]]++;
		for (int j = 1; j <= 100; j++) 
			if (num[j] != 0) v.push_back({num[j], j});

		sort(v.begin(), v.end());

		int v_size = v.size();
		if (max_c < v_size) max_c = v_size;
		for (int j = 0; j < v_size; j++) {
			arr[i][j * 2] = v[j].second;
			arr[i][j * 2 + 1] = v[j].first;
		}
		for (int j = (v_size * 2); j <= 100; j++) arr[i][j] = 0;\
	}
	c_cnt = max_c * 2;
}

void cal_C() {
	int max_r = 0;
	for (int j = 0; j < c_cnt; j++) {
		init();
		for (int i = 0; i < r_cnt; i++) num[arr[i][j]]++;
		for (int i = 1; i <= 100; i++)
			if (num[i] != 0) v.push_back({ num[i], i });

		sort(v.begin(), v.end());

		int v_size = v.size();
		if (max_r < v_size) max_r = v_size;
		for (int i = 0; i < v_size; i++) {
			arr[i * 2][j] = v[i].second;
			arr[i * 2 + 1][j] = v[i].first;
		}
		for (int i = (v_size * 2); i <= 100; i++) arr[i][j] = 0;
	}
	r_cnt = max_r * 2;
}

int main(void) {
	cin.tie(NULL);
	ios::sync_with_stdio(false);

	// input
	cin >> r >> c >> k;
	r--; c--;
	for (int i = 0; i < 3; i++)
		for (int j = 0; j < 3; j++) cin >> arr[i][j];

	while (arr[r][c] != k && result <= 100) {
		result++;
		if (r_cnt >= c_cnt) cal_R();
		else cal_C();
	}

	if (result == 101) result = -1;
	cout << result << '\n';

	return 0;
}