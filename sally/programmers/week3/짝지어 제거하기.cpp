#include <iostream>
#include <string>
#include <stack>
using namespace std;

int solution(string s) {
    int answer = 0;
    stack<int> st;
    int s_len = s.size();
    for(int i = 0; i < s_len; i++){
        if(st.empty()) {
            st.push(s[i]);
            continue;
        }
        
        if(st.top() == s[i]) st.pop();
        else st.push(s[i]);   
    }
    
    if(st.empty()) answer = 1;
    
    return answer;
}