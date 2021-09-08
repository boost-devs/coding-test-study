/*
# Simulation
# Problem: 16235
# Memory: 2336KB
# Time: 92ms
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
using namespace std;

int N, M, K;
deque<int> tree[11][11];
deque<pair<int, pair<int, int>>> dq;
int feed[11][11] = { 5 };
int winter_feed[11][11] = { 0 };
int xy[8][2] = { {0,1},{1,0},{-1,0},{0,-1},{-1,-1},{1,1},{-1,1},{1,-1} };
int result = 0;

void one_year() {
	// spring & summer
	for(int i = 0; i < N; i++)
		for (int j = 0; j < N; j++) {
			if (!tree[i][j].empty()) {
				int t_size = tree[i][j].size();
				bool kill_remain = false;
				for (int k = 0; k < t_size; k++) {
					int f_age = tree[i][j].front();
					tree[i][j].pop_front();
					if (kill_remain == false) {
						if (f_age <= feed[i][j]) {
							feed[i][j] -= f_age;
							tree[i][j].push_back(f_age + 1); // spring
						}
						else {
							kill_remain = true;
							feed[i][j] += (f_age / 2);
						}
					}
					else feed[i][j] += (f_age / 2); // summer

				}
			}
		}

	// fall & winter
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++) {
			feed[i][j] += winter_feed[i][j]; // winter
			if (!tree[i][j].empty()) {
				int t_size = tree[i][j].size();
				for (int k = 0; k < t_size; k++)
					if (tree[i][j][k] % 5 == 0)
						for (int t = 0; t < 8; t++) {
							int next_x = i + xy[t][0];
							int next_y = j + xy[t][1];
							if(0 <= next_x && next_x < N && 0 <= next_y && next_y < N)
								tree[next_x][next_y].push_front(1);
						}

							
			}
		}
			
}

int main(void) {
	cin.tie(NULL);
	ios::sync_with_stdio(false);

	cin >> N >> M >> K;
	for(int i = 0; i < N; i++)
		for (int j = 0; j < N; j++) {
			cin >> winter_feed[i][j];
			feed[i][j] = 5;
		}
	for (int i = 0; i < M; i++) {
		int a, b, c; cin >> a >> b >> c;
		dq.push_back({ c, {a-1, b-1} });
	}
	sort(dq.begin(), dq.end());
	for (int i = 0; i < M; i++) 
		tree[dq[i].second.first][dq[i].second.second].push_back(dq[i].first);

	for (int i = 0; i < K; i++) 
		one_year();

	for (int i = 0; i < N; i++){
		for (int j = 0; j < N; j++) 
			if (!tree[i][j].empty()) result += tree[i][j].size();
	}
	cout << result << '\n';

	return 0;
}