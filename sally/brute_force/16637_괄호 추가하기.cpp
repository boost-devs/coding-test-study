/*
# Brute force
# Problem: 16637
# Memory: 2028KB
# Time: 0ms
*/
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <string>
#include <queue>
#include <stack>
using namespace std;

int N, result = -1e9;
string str;
vector<int> nums;
vector<char> ops;
vector<bool> sel;
int op_len = 0;

int cal(int a, int b, char op){
	if(op == '+') return a + b;
	else if(op == '-') return a - b;
	else if(op == '*') return a * b;
}

int func(vector<int> nns){
	for(int i = 0; i < op_len; i++)
		if(sel[i])
			nns[i] = cal(nns[i], nns[i+1], ops[i]);

	int ret = nns[0];
	for(int i = 0; i < op_len; i++){
		if (sel[i]) continue;
		ret = cal(ret, nns[i+1], ops[i]);
	}
	return ret;
}

int main(void){
	cin.tie(NULL);
    ios::sync_with_stdio(false);

	cin >> N >> str;
	for(int i = 0; i < N; i++)
		if(i % 2 == 0) nums.push_back(atoi(&str[i]));
		else ops.push_back(str[i]);
	op_len = ops.size();
	
	if(N == 1) {
		cout << nums[0];
		return 0;
	}

	for(int i = 0; i < op_len; i++){
		sel.clear();
		for(int j = 0; j < i; j++) sel.push_back(true);
		for(int j = i; j < op_len; j++) sel.push_back(false);
		do{
			bool flag = false;
			for(int j = 1; j < op_len; j++) 
				if(sel[j-1] && sel[j]) {
					flag = true;
					break;
				}
			if(flag) continue;

			vector<int> nns;
			for(auto i : nums) nns.push_back(i);

			result = max(result, func(nns));
		} while (prev_permutation(sel.begin(), sel.end()));
	}
	
	cout << result;
	return 0;
}
