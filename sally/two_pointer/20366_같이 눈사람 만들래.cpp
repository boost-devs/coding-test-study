/*
# Two pointer
# Problem: 20366
# Memory: 2024KB
# Time: 180ms
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
vector<int> v;
vector<pair<int, int>> pairs;
int result = 1e9;

int main(void) {
	cin.tie(NULL);
    ios::sync_with_stdio(false);

	cin >> N;
	for(int i = 0; i < N; i++){
		int a; cin >> a;
		v.push_back(a);
	}
	sort(v.begin(), v.end());

	for(int i = 0; i < N-3; i++){
		for(int j = i+3; j < N; j++){
			int l = i+1;
			int r = j-1;
			while(l < r){
				int tmp = v[i] + v[j] - (v[l] + v[r]);
				result = min(result, abs(tmp));
				if(tmp > 0) l++;
				else r--;
			}
		}
	}

	cout << result << '\n';

	return 0;
}