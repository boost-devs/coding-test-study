/*
# Implementation
# Problem: 12933
# Memory: 2024KB
# Time: 0ms
*/
#include <iostream>
#include <vector>
#include <string>
using namespace std;

#define duck "quack"

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

	string str; cin >> str;
	int n = str.size();
	vector<bool> visit(n, false);
	vector<bool> start_v(n, false);
	// for(int i = 0; i < n; i++)
	// 	if(str[i] == 'q') start_v[i] = true;
	
	int ret = 0;
	for(int t = 0; t < n; t++){
		if(visit[t] == true || str[t] != 'q') continue;
		ret++;
		int j = 0;
		int target[5];
		for(int i = t; i < n; i++){
			if(visit[i] == false && str[i] == duck[j]){
				if(j == 4){
					target[j] = i;
					j = 0;
					for(int k = 0; k < 5; k++) visit[target[k]] = true;
				} else{
					target[j] = i;
					j++;
				}
			}
		}
	}

	for(int i = 0; i < n; i++) if(visit[i] == false) ret = -1;
	cout << ret;

    return 0;
}