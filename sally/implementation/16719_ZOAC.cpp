/*
# Implementation
# Problem: 16719
# Memory: 2024KB
# Time: 0ms
*/
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <string.h>
using namespace std;

#define INF 1e9

string str;
bool tf[101] = {false,};
int N;

void checker(int a, int b){
	int min_val = INF; int ind = INF;
	for(int i = a; i < b; i++){
		int target = str[i]-'A';
		if(!tf[i] &&  min_val > target){
			min_val = target;
			ind = i;
		}
	}
	
	if(min_val == INF) return;
	tf[ind] = true;

	for(int j = 0; j < N; j++)
		if(tf[j]) cout << str[j];
	cout << '\n';

	checker(ind+1, b);
	checker(a, ind);
}

int main(void) {
	cin.tie(NULL);
    ios::sync_with_stdio(false);

	cin >> str;
	N = str.size();

	checker(0, N);


	return 0;
}