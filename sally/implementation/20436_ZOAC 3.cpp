/*
# Implementation
# Problem: 20436
# Memory: 2024KB
# Time: 0ms
*/
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;

#define left_keys "qwertasdfgzxcv"
#define LK_len 14

string key_l[3] = {"qwert", "asdfg", "zxcv"};
string key_r[3] = {" yuiop", " hjkl", "bnm"};

pair<int, int> cur_l, cur_r;
pair<int, int> next_loc;
string str;
int result = 0;

pair<int, int> find_loc(bool is_L, char c){
	if(is_L){
		for(int i = 0; i < 3; i++)
			for(int j = 0; j < key_l[i].size(); j++)
				if(key_l[i][j] == c) 
					return {i, j};
	} else{
		for (int i = 0; i < 3; i++)
			for (int j = 0; j < key_r[i].size(); j++)
				if (key_r[i][j] == c)
					return {i, j};
	}
}

int main(void) {
	cin.tie(NULL);
    ios::sync_with_stdio(false);

	char c1, c2;
	cin >> c1 >> c2 >> str;

	cur_l = find_loc(true, c1);
	cur_r = find_loc(false, c2);

	int s_len = str.size();
	for(int t = 0; t < s_len; t++){
		bool isLeft = false;
		for (int i = 0; i < LK_len; i++)
			if(left_keys[i] == str[t]) isLeft = true;

		next_loc = find_loc(isLeft, str[t]);
		if(isLeft){
			result += (abs(next_loc.first - cur_l.first) + abs(next_loc.second - cur_l.second));
			cur_l = next_loc;
		} else{
			result += (abs(next_loc.first - cur_r.first) + abs(next_loc.second - cur_r.second));
			cur_r = next_loc;
		}
	}

	cout << result + s_len;

	return 0;
}