/*
# String
# Problem: 17413
# Memory: 2624KB
# Time: 0ms
*/
#include <iostream>
#include <string.h>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

string str;
string result = "";
stack<char> st;
queue<char> q;

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    getline(cin, str);
    str += 'X';
    int i = 0;
    while(str[i] != 'X'){
        // < >
        if(str[i] == '<'){
            if(!st.empty()){
                while(!st.empty()){
                        result += st.top();
                        st.pop();
                    }
            }
            while(str[i] != '>'){
                q.push(str[i]);
                i++;
            }
            q.push('>');
            while(!q.empty()){
                result += q.front();
                q.pop();
            }
        }
        // space
        else if(str[i] == ' '){
            while(!st.empty()){
                result += st.top();
                st.pop();
            }
            result += ' ';
        }
        // chars
        else{
            st.push(str[i]);
        }

        i++;
    }
    if(!st.empty()){
        while(!st.empty()){
                result += st.top();
                st.pop();
                i++;
            }
    }

    cout << result << '\n';

    return 0;
}