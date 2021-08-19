/*
# Brute force
# Problem: 15686
# Memory: 2024KB
# Time: 4ms
*/
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <string>
using namespace std;

int N, M;
vector<pair<int, int>> chicken_house;
vector<pair<int, int>> home;
vector<bool> chicken_selector;
int result = 1e9;

int chicken_dist(pair<int, int> p){
	int ret = 1e9;
	int ch_len = chicken_house.size();

	for(int i = 0; i < ch_len; i++)
		if(chicken_selector[i])
			ret = min(ret, abs((p.first - chicken_house[i].first)) + abs((p.second - chicken_house[i].second)));

	return ret;
}


int all_dist(){
	int ret = 0;
	for(auto i: home){
		ret += chicken_dist(i);
		if(ret > result) break;
	}
	return ret;	
}


int main(void){
	cin.tie(NULL);
    ios::sync_with_stdio(false);

	cin >> N >> M;
	for(int i = 0; i < N; i++)
		for(int j = 0; j < N; j++) {
			int a; cin >> a;
			if(a == 1) home.push_back({i, j});
			else if(a == 2) chicken_house.push_back({i, j});
		}
	int ch_len = chicken_house.size();
	for(int i = 0; i < ch_len; i++)
		chicken_selector.push_back(false);
	for(int i = 0; i < M; i++)
		chicken_selector[i] = true;

	do{
		result = min(result, all_dist());
	}while(prev_permutation(chicken_selector.begin(), chicken_selector.end()));
			
	cout << result << '\n';
	return 0;
}