/*
# Brute force
# Problem: 2422
# Memory: 3088KB
# Time: 32ms
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

int N, M;
vector<pair<int, int>> v;
int result = 0;
set<int> s[201];

void dfs(int a, int b, int dep){
	if(dep == 1)
		for(int i = a + 1; i <= N; i++)
			if(s[a].find(i) == s[a].end())
				dfs(a, i, 2);
	else if(dep == 2){
		for(int i = b+1; i <= N; i++)
			if(s[a].find(i) == s[a].end() && s[b].find(i) == s[b].end())
				result++;
	}
}


int main(void) {
	cin.tie(NULL);
    ios::sync_with_stdio(false);

	cin >> N >> M;
	for(int i = 0; i < M; i++){
		int a, b; cin >> a >> b;
		s[a].insert(b);
		s[b].insert(a);
	}

	for(int i = 1; i <= N; i++)
		dfs(i, 0, 1);

	cout << result << '\n';
	return 0;
}