/*
# Two pointer
# Problem: 21921
# Memory: 3684KB
# Time: 24ms
*/
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <string>
using namespace std;

#define SAD "SAD"

int max_num = 0;
int sames = 1;
int N, X;
vector<int> v;

int main(void) {
	cin.tie(NULL);
    ios::sync_with_stdio(false);

	cin >>N >>X;
	v.push_back(0);
	for(int i = 0; i <N; i++){
		int a; cin >> a;
		v.push_back(a + v[v.size()-1]);
	}

	for(int i = X; i <= N; i++){
		int target = v[i] - v[i-X];
		if(max_num < target){
			max_num = target;
			sames = 1;
		}else if(max_num == target) sames++;
	}
		
	if(max_num == 0) cout << SAD;
	else cout << max_num << '\n' << sames;

		

	return 0;
}