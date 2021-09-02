/*
# Brute force
# Problem: 18808
# Memory: 2164KB
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

#define sq vector<vector<bool>>

int N, M, K;
vector<sq> squares;
bool visit[41][41] = {false};
int result = 0;

bool find_loc(int ind){
	int n = squares[ind].size();
	int m = squares[ind][0].size();
	
	// start loc(paper's)
	bool success = false;
	int i, j;
	for(i = 0; i <= N-n; i++){
		for(j = 0; j <= M-m; j++){
			
			// check all loc(block's)
			bool flag = true;
			for(int a = 0; a < n; a++){
				for(int b = 0; b < m; b++)
					if(squares[ind][a][b] && visit[i+a][j+b]) {
						flag = false; // impossible case
						break;
					}
				if(!flag) break;
			}
			if(flag) {
				success = true;
				break;
			}
		}
		if(success) break;
	}
		
	// make visit true
	if(success)
		for(int a = 0; a < n; a++)
			for(int b = 0; b < m; b++)
				if(squares[ind][a][b]){
					visit[i+a][j+b] = true;
					result ++;
				}

	if(success) return true;
	else return false;
}

void rotate_sq(int ind) {
	sq target = squares[ind];
	int n = target.size();
	int m = target[0].size();

	// rotate target
	sq res;
	for(int i = 0; i < m; i++){
		vector<bool> res1;
		for(int j = 0; j < n; j++)
			res1.push_back(false);
		res.push_back(res1);
	}
	int cnt = 0;
	for(int i = n-1; i >= 0; i--){
		for(int j = 0; j < m; j++){
			res[j][cnt] = target[i][j];
		}
		cnt++;
	}
	
	squares[ind] = res;
}

void func(int ind){
	for(int i = 0; i < 4; i++){
		if(find_loc(ind)) break;
		rotate_sq(ind);
	}
}

int main(void){
	cin.tie(NULL);
    ios::sync_with_stdio(false);

	// init
	cin >> N >> M >> K;
	for(int i = 0; i < K; i++){
		int r, c; cin >> r >> c;
		sq tmp2;
		for(int a = 0; a < r; a++){
			vector<bool> tmp; int d;
			for(int b = 0; b < c; b++){
				cin >> d;
				if(d == 1) tmp.push_back(true);
				else tmp.push_back(false);
			}
			tmp2.push_back(tmp);
		}
		squares.push_back(tmp2);	
	}
	
	// for all squares
	for(int i = 0; i < K; i++)
		func(i);

	cout << result <<'\n';

	return 0;
}