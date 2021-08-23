/*
# Brute force
# Problem: 14391
# Memory: 2032KB
# Time: 64ms
*/
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <string>
#include <queue>
#include <stack>
using namespace std;

int N, M;
string str;
vector<string> arr;
vector<bool> visit1;
vector<vector<bool>> visit;
int result = 0;

int cal(){
	int ret = 0;
	// calculate left -> right
	for(int i = 0; i < N; i++){
		string st = "";
		for(int j = 0; j < M; j++){
			if(visit[i][j]) st += arr[i][j];
			else if(st != ""){
				ret += stoi(st);
				st = "";
			}
		}
		if(st != "") ret += stoi(st);
	}

	// calculate up -> down
	for(int j = 0; j < M; j++){
		string st = "";
		for(int i = 0; i < N; i++){
			if(visit[i][j] == false) st += arr[i][j];
			else if(st != "") {
				ret += stoi(st);
				st = "";
			}
		}
		if(st != "") ret += stoi(st);
	}
	return ret;
}

void cutter(){
	visit.clear();
	for(int i = 0; i < N; i++){
		vector<bool> tmp;
		for(int j = 0; j < M; j++)
			tmp.push_back(visit1[M*i + j]);
		visit.push_back(tmp);
	}

	result = max(result, cal());
	return;
}

int main(void){
	cin.tie(NULL);
    ios::sync_with_stdio(false);

	cin >> N >> M;
	for(int i = 0; i < N; i++){
		cin >> str;
		arr.push_back(str);
	}

	for(int i = 0; i <= N*M; i++){
		visit1.clear();
		for(int j = 0; j < i; j++) visit1.push_back(true);
		for(int j = i; j < N*M; j++) visit1.push_back(false);
		do{
			cutter();
		} while (prev_permutation(visit1.begin(), visit1.end()));
	}
	
	cout << result << '\n';

	return 0;
}