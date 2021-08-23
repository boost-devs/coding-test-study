/*
# Brute force
# Problem: 21315
# Memory: 2340KB
# Time: 4ms
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

int N, K = 1;
vector<int> v, target;

vector<int> shuffler(vector<int> ori, int k){
	vector<int> dst, src;
	vector<int> tmp_last;

	for(auto i: ori) src.push_back(i);

	// 맨 위에 있던거 저장
	for(int i = 0; i < N - pow(2, k); i++)
		tmp_last.push_back(src[i]);

	// 맨 아래에 있던거 맨 위로 올리기
	dst.push_back(src[N-1]);

	// 1, 2, 4, ... 뒤에서부터 잘라서, 기저 순서를 지켜서
	int start_point = N-2;
	for(int i = 0; i < k; i++){
		int end_point = start_point + pow(2, i);
		for (int j = start_point; j < end_point; j++)
			dst.push_back(src[j]);
		start_point -= pow(2, i+1);
	}

	// 맨 위에 있던거 맨 아래 붙이기
	for (auto i : tmp_last)
		dst.push_back(i);

	return dst;
}

bool game_end(vector<int> a, vector<int> b){
	for(int i = 0; i < N; i++)
		if(a[i] != b[i]) return false;
	return true;
}

int main(void){
	cin.tie(NULL);
    ios::sync_with_stdio(false);

	cin >> N;
	for(int i = 1; i <= N; i++) {
		int a; cin >> a;
		target.push_back(a);
		v.push_back(i);
	}

	for(K = 1; K < N; K++)
		if(pow(2, K) >= N) {
			K--;
			break;
		}

	bool flag = false;
	for(int i = 1; i <= K; i++){
		vector<int> result1 = shuffler(v, i);
		for (int j = 1; j <= K; j++){
			vector<int> result2 = shuffler(result1, j);
			if(game_end(target, result2)){
				cout << i << ' ' << j;
				flag = true;
				break;
			}
		}
		if(flag) break;
	}
		

	return 0;
}