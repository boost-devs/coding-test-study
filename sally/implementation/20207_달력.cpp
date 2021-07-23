/*
# Implementation
# Problem: 20207
# Memory: 2020KB
# Time: 0ms
*/
#include <iostream>
#include <vector>
#include <deque>
#include <cmath>
using namespace std;

#define MAX 367
int N;
int a, b;
int arr[MAX] = {0,};

int height = 0;
int width = 0;
int result = 0;

int main(void) {
	cin.tie(NULL);
    ios::sync_with_stdio(false);

	cin >> N;
	for(int i = 0; i < N; i++) {
		cin >> a >> b;
		for(int j = a; j <= b; j++)
			arr[j]++;
	}

	for(int i = 1; i < MAX; i++){
		if(arr[i] == 0){
			result += height * width;
			height = width = 0;
			continue;
		}
		width++;
		height = max(height, arr[i]);
	}
	cout << result;

	return 0;
}
