/*
# Implementation
# Problem: 11659
# Memory: 2800KB
# Time: 52ms
*/
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <string>
using namespace std;

#define ll long long
#define MAX 100002

ll arr[MAX] = {0, };
int N, M;

int main(void) {
	cin.tie(NULL);
    ios::sync_with_stdio(false);

	cin >>N >> M;
	for(int i = 1; i <= N; i++){
		cin >> arr[i];
		arr[i] += arr[i-1];
	}

	for(int i = 0; i < M; i++){
		int a, b;
		cin >> a >> b;
		cout << arr[b] - arr[a-1] << '\n';
	}
		

	return 0;
}