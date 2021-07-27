/*
# Implementation
# Problem: 20164
# Memory: 2028KB
# Time: 0ms
*/
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <string.h>
using namespace std;

string s;
#define INF 1e9
int min_val = INF, max_val = 0;


// count odd num in str
int odd_count(string str){
	int n = 0;
	int s_size = str.size();
	for(int i = 0; i < s_size; i++)
		if(str[i] % 2 == 1)
			n++;
	return n;
}

// update min, max value
void updater(int num){
	min_val = min(min_val, num);
	max_val = max(max_val, num);
}

// recursively make str
void func(string str, int cur_odd){
	/* 1 */
	cur_odd = cur_odd + odd_count(str+'0');

	int N = str.size();
	if(N == 1) { /* 2 */
		updater(cur_odd);
	}
	else if(N == 2){ /* 3 */
		int a = str[0] - '0';
		int b = str[1] - '0';
		str = to_string(a+b);

		func(str, cur_odd);
		
	}else{ /* 4 */
		for(int i = 1; i < N-1; i++){
			for(int j = i+1; j < N; j++){
				int a = stoi(str.substr(0, i));
				int b = stoi(str.substr(i, j-i));
				int c = stoi(str.substr(j, N-j));
				string tmp_s = to_string(a + b + c);

				func(tmp_s, cur_odd);
			}
		}
	}
}

int main(void) {
	cin.tie(NULL);
    ios::sync_with_stdio(false);

	cin >> s;
	func(s, 0);

	cout<< min_val << ' ' << max_val << '\n';
	return 0;
}

// substr(pos, cnt)
// [pos, pos + cnt)
