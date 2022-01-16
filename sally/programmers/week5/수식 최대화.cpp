#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <stack>
#include <queue>
#include <typeinfo>
using namespace std;

long long solution(string expression) {
    long long answer = 0;
    char sample_ops[3] = {'+', '-', '*'};
    
    // Permutation declare
    vector<int> seq; // + - *
    seq.push_back(0); seq.push_back(1); seq.push_back(2);
    
    // cut words
    expression += '-'; // for last number push_back
    vector<string> s;
    int ex_len = expression.size();
    int cur = 0;
    int cnt = 0;
    for(int i = 0; i < ex_len; i++){
        cnt++;
        for(int j = 0; j < 3; j++){
            if(expression[i] == sample_ops[j]){
                s.push_back(expression.substr(cur, cnt-1));
                string ss = "";
                ss += expression[i];
                s.push_back(ss);
                cur += cnt;
                cnt = 0;
                break;
            }
        }
    }
    s.pop_back(); // for last op(non-use) pop_back
    
    // make num => long long // make ops => char
    vector<long long> nums_;
    vector<char> ops_;
    int s_len = s.size();
    for(int i = 0; i < s_len; i++)
        if(i % 2 == 0){
            long long n = stoll(s[i]);
            nums_.push_back(n);
        } else ops_.push_back(s[i][0]);
    
    // permutation loop
    do{ 
        // init
        vector<long long> nums;
        vector<char> ops;
        for(auto i : nums_) nums.push_back(i);
        for(auto i : ops_) ops.push_back(i);
        
        // for all operations
        for(int t = 0; t < 3; t++){
            stack<long long> st_ll;
            stack<char> st_c;
            char target = sample_ops[seq[t]];
            // cout << typeid(target).name() << '\n';
            // cout << typeid(char(ops[t])).name() << '\n';
            
            st_ll.push(nums[0]); // push first num
            
            int ops_len = ops.size();
            for(int i = 0; i < ops_len; i++){ // loop -> ops size
                long long n = nums[i+1];
                char c = ops[i];
                
                if(c == target) {
                    long long n1 = st_ll.top();
                    st_ll.pop();
                    if(target == '+') n1 += n;
                    else if(target == '-') n1 -= n;
                    else n1 *= n;
                    st_ll.push(n1);
                } else{
                    st_ll.push(n);
                    st_c.push(c);
                }
            }
            
            // init stacks with new elements
            
            stack<long long> st_ll2;
            stack<char> st_c2;
            while(!st_ll.empty()){
                st_ll2.push(st_ll.top());
                st_ll.pop();
            }
            while(!st_c.empty()){
                st_c2.push(st_c.top());
                st_c.pop();
            }
            
            nums.clear(); ops.clear();
            while(!st_ll2.empty()) {
                nums.push_back(st_ll2.top());
                st_ll2.pop();
            }
            while(!st_c2.empty()) {
                ops.push_back(st_c2.top());
                st_c2.pop();
            }
        }
        answer = max(answer, abs(nums[0]));
    }while(next_permutation(seq.begin(), seq.end()));
    
    
    
    
    return answer;
}