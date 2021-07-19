/*
# Implementation
# Problem: 10994
# Memory: 2288KB
# Time: 0ms
*/
#include <iostream>
#include <vector>
#include <string>
using namespace std;

#define s1 "* "
#define s2 " *"

int N, M;
vector<string> v;

string get_empty(int n){
	string s;
	for(int i = 0; i < n; i++) s += ' ';
	return s;
}
string get_full(int n){
	string s;
	for (int i = 0; i < n; i++) s += '*';
	return s;
}

int main(void) {
	cin.tie(NULL);
    ios::sync_with_stdio(false);

	cin >> N;
	M = 4 * (N - 1) + 1;
	
	v.push_back(get_full(M));

	for(int i = 1; i < N; i++){
		string str;
		for(int j = 0; j < i; j++) str += s1;
		str += get_empty(M-(i*4));
		for(int j = 0; j < i; j++) str += s2;
		v.push_back(str);
		str = "";
		for(int j = 0; j < i; j++) str += s1;
		str += get_full(M-(i*4));
		for(int j = 0; j < i; j++) str += s2;
		v.push_back(str);
	}

	int a = v.size();
	for(int i = a-2; i >= 0; i--) v.push_back(v[i]);
	for(auto i : v) cout <<i << '\n';

	return 0;
}