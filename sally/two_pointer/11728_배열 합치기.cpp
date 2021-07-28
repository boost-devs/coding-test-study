/*
# Implementation
# Problem: 11728
# Memory: 14436KB
# Time: 672ms
*/
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <string.h>
using namespace std;

int N, M, a;
vector<int> A;

int main(void) {
	cin.tie(NULL);
    ios::sync_with_stdio(false);

	cin >> N >> M;
	for(int i = 0; i < N+M; i++) {
		cin >> a;
		A.push_back(a);
	}
	sort(A.begin(), A.end());
	for(auto i: A)
	 	cout << i <<' ';
	cout << '\n';

	return 0;
}