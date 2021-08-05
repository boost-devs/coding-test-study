/*
# Two pointer
# Problem: 20442
# Memory: 31728KB
# Time: 68ms
*/
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <string>
#include <queue>
using namespace std;

#define MAX 3000001

string str;
int a_ind = 0;
int b_ind = 0;


int R[MAX] = {0,};
int K[MAX] = {0,};

int max_lr = 0;
int r_cnt = 0;
int k_cnt = 0;
int result = 0;

int main(void) {
	cin.tie(NULL);
    ios::sync_with_stdio(false);
	
	cin >> str;
	int s_len = str.size();

	for(int i = 0; i < s_len; i++){
		if (str[i] == 'R')
			r_cnt++;
		if (str[i] == 'K')
			k_cnt++;
		R[i] = r_cnt;
		K[i] = k_cnt;
	}

	int a = 0;
	int b = s_len - 1;

	while(a <= b){
		int target = -1;
		int l = K[s_len - 1] - K[b];
		if (str[b] == 'K') l++; // 예외처리 중요 // KKKR
		if (R[b] - R[a] > 0)
			target = R[b] - R[a] + (2 * min(K[a], l));
		result = max(result, target);
		
		if(K[a] < l) a++;
		else b--;
	}

	cout << max(result, r_cnt);

	return 0;
}