/*
# Brute force
# Problem: 5568
# Memory: 2292KB
# Time: 4ms
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

int N, K;
int card[11] = {0,};
set<string> s;
vector<string> v;

void DFS(string cur, int num[4], int dep){
	if(dep == K) {
		s.insert(cur);
		return;
	}
	for(int i = 0; i < N; i++){
		if(i == num[0] || i == num[1] || i == num[2]) continue;
		num[dep] = i;
		DFS(cur + v[i], num, dep+1);
		DFS(v[i] + cur, num, dep + 1);
	}
}


int main(void) {
	cin.tie(NULL);
    ios::sync_with_stdio(false);

	cin >> N >> K;
	for(int i = 0 ; i < N; i++){
		string str; cin >> str;
		v.push_back(str);
	}

	for(int i = 0; i < N; i++){
		int num[4] = {i, -1, -1, -1};
		DFS(v[i], num, 1);
	}

	cout << s.size();

	return 0;
}