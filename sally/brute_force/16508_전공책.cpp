/*
# Brute force
# Problem: 16508
# Memory: 2024KB
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

string str;
int N;
vector<int> price;
vector<string> book;
int need[26] = {0,};
int result = 1e9;

bool checker(int used[26]){
	bool ret = true;
	for(int i = 0; i < 26; i++)
		if(need[i] > used[i]) ret = false;

	return ret;
}

void DFS(int cur, int total, int used[26]){
	if(cur == N) return;

	int b_len = book[cur].size();
	int param[26] = {0,};
	for(int i = 0; i < 26; i++) param[i] = used[i];
	for(int i = 0; i < b_len; i++) param[book[cur][i] - 'A']++;
	total = total + price[cur];

	if (checker(param)) {
		result = min(total, result);
		return;
	}
	else{
		for(int i = cur + 1; i < N; i++)
			DFS(i, total, param);

		return;	
	}

	
}

int main(void) {
	cin.tie(NULL);
    ios::sync_with_stdio(false);

	cin >> str >> N;
	for(int i = 0; i < N; i++){
		int a; string s;
		cin >> a >> s;
		price.push_back(a);
		book.push_back(s);	
	}

	int s_len = str.size();
	for(int i = 0; i < s_len; i++) need[str[i] - 'A']++;

	int tmp[26] = {0,};
	for(int i = 0; i < N; i++)
		DFS(i, 0, tmp);
	
	if(result == 1e9) cout << -1 << '\n';
	else cout << result;

	// for(int i = 0; i < 26; i++) cout << need[i] << ' ';

	return 0;
}