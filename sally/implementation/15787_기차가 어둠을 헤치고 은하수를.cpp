/*
# Implementation
# Problem: 15787
# Memory: 4460KB
# Time: 16ms
*/
#include <iostream>
#include <vector>
#include <string>
using namespace std;

#define RANGER (1 << 20)-1

int N, M, cmd, train, target;
bool visit[1<<21] = {false,};
int result = 0;

int main(void) {
	cin.tie(NULL);
    ios::sync_with_stdio(false);

	cin >> N >> M;
	vector<int> v(N+1, 0);
	for(int t = 0; t < M; t++){
		cin >> cmd >> train;
		if(cmd == 1){ // bit on
			cin >> target;
			v[train] |= (1 << (target-1));
		} else if(cmd == 2){ // bit off
			cin >> target;
			v[train] &= ~(1 << (target-1));
			v[train] &= RANGER;
		} else if(cmd == 3){ // <
			v[train] = v[train] << 1;
			v[train] &= RANGER;
		} else{ // >
			v[train] = v[train] >> 1;
		}
	}

	for(int i = 1; i <= N; i++)
		if(visit[v[i]] == false){
			visit[v[i]] = true;
			result ++;
		}

	cout << result << '\n';

	return 0;
}