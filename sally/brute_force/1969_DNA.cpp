/*
# Brute force
# Problem: 1969
# Memory: 2188KB
# Time: 0ms
*/
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <string>
#include <queue>
using namespace std;

#define A 0
#define C 2
#define G 6
#define T 19

int DNA[20] = {0, };
int N, M;
string str[1001];
int ham_dist = 0;

void init(){
	DNA[A] = DNA[C] = DNA[G] = DNA[T] = 0;
}

pair<char, int> max_char_ham(){
	int arr[4] = {A, C, G, T};
	int max_val = DNA[A]; int max_ind = A;
	for(int i = 1; i < 4; i++)
		if(DNA[arr[i]] > max_val){
			max_val = DNA[arr[i]];
			max_ind = arr[i];
		}
	return {max_ind + 'A', N-max_val};
}

int main(void) {
	cin.tie(NULL);
    ios::sync_with_stdio(false);

	cin >> N >> M;
	for(int i = 0; i < N; i++)
		cin >> str[i];
        
	string result = "";
	for(int i = 0; i < M; i++){
		init();
		for(int j = 0; j < N; j++)
			DNA[str[j][i] - 'A']++;

		pair<char, int> p = max_char_ham();
		result += p.first;
		ham_dist += p.second;
	}

	cout << result << '\n' << ham_dist << '\n';

	return 0;
}