/*
# Brute force
# Problem: 2503
# Memory: 2156KB
# Time: 0ms
*/
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <string>
#include <queue>
using namespace std;

int N, S, B;
string str;
vector< pair<string, pair<int, int>>> v;
int result = 0;

bool checker(string src, pair<string, pair<int, int>> dst){
	int ball = 0;
	int st = 0;
	for(int i = 0; i < 3; i++){
		if (src[i] == dst.first[i]) st++;
		for (int j = 0; j < 3; j++)
			if (src[i] == dst.first[j])
				ball++;
	}
	if(dst.second.first == st && dst.second.second == (ball - st)) return true;
	else return false;
}

int main(void) {
	cin.tie(NULL);
    ios::sync_with_stdio(false);

	cin >> N;
	for(int i = 0; i < N; i++){
		cin >> str >> S >> B;
		v.push_back({str, {S, B}});
	}

	for(int i = 111; i <= 999; i++){
		string target = to_string(i);
		if (target[0] == '0' || target[1] == '0' || target[2] == '0') continue;
		if (target[0] == target[1] || target[1] == target[2] || target[2] == target[0]) continue;
		bool flag = true;
		for(auto j: v)
			if(!checker(target, j)) flag = false;
		if(flag) result++;
	}

	cout << result<< '\n';

	return 0;
}