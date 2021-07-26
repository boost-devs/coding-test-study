/*
# Implementation
# Problem: 1244
# Memory: 2020KB
# Time: 0ms
*/
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int N, M, who, num;
bool state[101] = {false,};

void woman(){
	state[num] = !state[num];
	for(int i = 1; i <= N; i++){
		if(0<num-i && num+i<=N){
			if (state[num - i] == state[num + i]){
				state[num - i] = !state[num - i];
				state[num + i] = !state[num + i];
			} else break;
		} else break;
	}
}

void man(){
	for(int i = 1; i <= N; i++){
		if(num * i > N) break;
		state[num * i] = !state[num * i];
	}
}

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

	cin >> N;
	for(int i = 1; i <= N; i++) cin >> state[i];
	cin >> M;
	for(int t = 0; t < M; t++){
		cin >> who >> num;
		if(who == 1) man();
		else woman();
	}

	for(int i = 1; i <= N; i++) {
		if(state[i] == true) cout << 1;
		else cout << 0;

		if(i % 20 == 0) cout << '\n';
		else if(i != N) cout << ' ';
	}

	return 0;
}