/*
# Implementation
# Problem: 14710
# Memory: 2024KB
# Time: 0ms
*/
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <string.h>
using namespace std;

#define MAX 500

int W, H;
int arr[MAX] = {0,};
int res[MAX] = {0,};

int main(void) {
	cin.tie(NULL);
    ios::sync_with_stdio(false);

	cin>> H >> W;
	for(int i = 0; i < W; i++)
		cin >> arr[i];

	for(int i = 0; i < W; i++) // =>
		for(int j = i+1; j < W; j++)
			if(arr[i] <= arr[j]){
				for(int k = i+1; k < j; k++)
					res[k] = max(res[k], arr[i] - arr[k]);
				break;
			}
	

	for(int i = W; i >= 0; i--) // <=
		for(int j = i-1; j >=0; j--)
			if(arr[i] <= arr[j]){
				for(int k = i-1; k > j; k--)
					res[k] = max(res[k], arr[i] - arr[k]);
				break;
			}

	int result = 0;
	for(int i = 0; i < W; i++)
		result+=res[i];
	cout << result <<'\n';

	return 0;
}