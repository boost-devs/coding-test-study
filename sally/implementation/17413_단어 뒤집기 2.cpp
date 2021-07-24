/*
# Implementation
# Problem: 17413
# Memory: 2516KB
# Time: 0ms
*/
#include <iostream>
#include <vector>
#include <string>
#include <string.h>
#include <stack>
#include <cmath>
#include <algorithm>
using namespace std;

string str, result;
int s_len;
stack<char> st;

int main(void) {
	cin.tie(NULL);
    ios::sync_with_stdio(false);

	getline(cin, str);
	s_len = str.size();
	for(int i = 0; i < s_len; i++){
		if(str[i] == '<'){ // <>
			while(!st.empty()){
				result += st.top();
				st.pop();
			}
			while(str[i] != '>') {
				result += str[i];
				i++;
			}
			result += '>';
		} else if(str[i] == ' ') { // ' '
			while(!st.empty()){
				result += st.top();
				st.pop();
			}
			result += str[i];
		} else st.push(str[i]);
	}
	while(!st.empty()){
		result += st.top();
		st.pop();
	}
	
	cout << result;

	return 0;
}
//<int><max>2147483647<long long><max>9223372036854775807
// <ab cd>fe hg<ij kl>