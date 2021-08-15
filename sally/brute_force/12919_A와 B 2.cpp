/*
# Brute force
# Problem: 12919
# Memory: 2024KB
# Time: 0ms
*/
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <string>
using namespace std;

string src, dst;
int result = 0;

void dfs(string cur){
	if(cur.size() == dst.size()){
		if(cur == dst) result = 1;
		return;
	}
	
	int last_ind = cur.size() - 1;
	if(cur[0] == 'A' && cur[last_ind] == 'B') return;
	if(cur[last_ind] == 'A') dfs(cur.substr(0, last_ind));
	if(cur[0] == 'B') {
		string nex = cur.substr(1, last_ind);
		reverse(nex.begin(), nex.end());
		dfs(nex);
	}
}

int main(void) {
	cin.tie(NULL);
    ios::sync_with_stdio(false);

	cin >> dst >> src;
	dfs(src);
	cout << result;

	return 0;
}