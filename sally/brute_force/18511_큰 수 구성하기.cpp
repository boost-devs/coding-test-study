/*
# Brute force
# Problem: 2208
# Memory: 2208KB
# Time: 0ms
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

int target;
int K;
vector<int> karr;
vector<int> knum;
int result = 0;
bool tf = false;


void DFS(int cur, int dep){
	if(cur >= target) return;
	for(int i = 0; i < K; i++){
		int cur1 = cur * pow(10, knum[i]) + karr[i];
		DFS(cur1, dep+1);
		if(cur1 <= target)
			result = max(result, cur1);
		else break;
	}
}

int main(void) {
	cin.tie(NULL);
    ios::sync_with_stdio(false);
	
	cin >> target >> K;
	for(int i = 0; i < K; i++){
		int a; cin >> a;
		karr.push_back(a);
	}
	sort(karr.begin(), karr.end());

	for(auto i : karr)
		knum.push_back(to_string(i).size());

	DFS(0, 0);
	cout << result;

	return 0;
}