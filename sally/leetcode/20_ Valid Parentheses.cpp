// 20. Valid Parentheses
// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Valid Parentheses.
// Memory Usage: 6.5 MB, less than 10.15% of C++ online submissions for Valid Parentheses.

#include <stack>
#include <string>

class Solution {
public:
    bool isValid(string s) {
        char opened_b[3] = {'[','{','('};
        char closed_b[3] = {']','}',')'};
        stack<int> st;
        int s_len = s.size();
        
        for(int i = 0; i < s_len; i++){
            bool opened = false;
            for(int j = 0; j < 3; j++)
                if(s[i] == opened_b[j]){
                    opened = true;
                    st.push(j);
                    break;
                }
            if(opened) continue;
            for(int j = 0; j < 3; j++)
                if(s[i] == closed_b[j]){
                    if(st.empty()) return false;
                    if(st.top() == j) st.pop();
                    else return false;
                }
        }
        if (st.empty()) return true;
        else return false;
    }
};