/*
# Two pointer
# Problem: 20922
# Memory: 3192KB
# Time: 20ms
*/
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <string>
#include <queue>
using namespace std;

int nums[100001] = {0,};
int seq[200001] = {0,};
int N, K;
int start_v = 0, end_v = 0;
int max_len = 0;

int main(void) {
	cin.tie(NULL);
    ios::sync_with_stdio(false);
	
	cin >> N >> K;
	for(int i = 0; i < N; i++){
		cin >> seq[i];
		if(nums[seq[i]] >= K){
			bool flag = true;
			while(flag){
				if(seq[start_v] == seq[i]) flag = false;
				nums[seq[start_v]]--;
				start_v++;
			}
		}
		end_v++;
		nums[seq[i]]++;
		
		max_len = max(max_len, end_v - start_v);
	}

	cout << max_len << '\n';
	

	return 0;
}