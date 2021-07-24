/*
# Implementation
# Problem: 2578
# Memory: 2020KB
# Time: 0ms
*/
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int arr[26];
int memo[26];
int result = 0;

bool checker(){
	int ind; bool res;
	int bing = 0;

	// col
	for(int i = 1; i <= 5; i++){
		res = true;
		for(int j = 0; j < 5; j++){
			ind = i + (j * 5);
			if(arr[ind] != 0) res = false;
		}
		if(res) bing++;
	}
		

	// row
	for(int i = 1; i < 25; i+=5){
		res = true;
		for(int j = 0; j < 5; j++){
			ind = i + j;
			if(arr[ind] != 0) res = false;
		}
		if(res) bing++;
	}
	
	// left-bottom dir
	res = true;
	for(int i = 1; i <= 25; i+=6)
		if(arr[i] != 0) res = false;
	if(res) bing++;

	// right-bottom dir
	res = true;
	for(int i = 5; i <= 21; i+=4)
		if(arr[i] != 0) res = false;
	if(res) bing++;

	if(bing >= 3) return true;
	else return false;
}

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

	for(int i = 1; i <= 25; i++) {
		cin >> arr[i];
		memo[arr[i]] = i;
	}
	for (int i = 1; i <= 25; i++){
		int num; cin >> num;
		arr[memo[num]] = 0;
		if(result == 0 && checker()) {
			result = i;
		}
	}
	
	cout << result;

	return 0;
}