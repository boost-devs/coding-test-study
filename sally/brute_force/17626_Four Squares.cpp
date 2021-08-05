/*
# Brute force
# Problem: 17626
# Memory: 2032KB
# Time: 84ms
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

int N;
int min_dep = 5;

void dfs(int cur, int ind, int dep){
	if(dep == 4 || dep >= min_dep) return;
	int st = floor(sqrt(cur));
	st = min(st, ind);
	for (int i = st; i > 0; i--){
		int target = cur - pow(i, 2);
		if(target == 0) {
			min_dep = min(min_dep, dep+1);
			break;
		}
		else dfs(target, i, dep + 1);
	}
}

int main(void) {
	cin.tie(NULL);
    ios::sync_with_stdio(false);

	cin >> N;
	dfs(N, N, 0);
	cout << min_dep;

	return 0;
}