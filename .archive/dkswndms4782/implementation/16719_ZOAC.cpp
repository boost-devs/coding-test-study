#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
using namespace std;

int main(){
    string str; cin >> str;
    stack<int>s;
    bool check[103] = {false,};
    check[str.length()] = true;
    s.push(-1);
    while(!s.empty()){
        int tmp = s.top();
        if(check[tmp+1]) {s.pop(); continue;}
        int Min = 1e9; int now;
        for(int i = tmp + 1;i<str.length() + 1;i++){
            if(check[i]) break;
            if(Min > str[i] - 'A'){
                now = i;
                Min = str[i] - 'A';
            }
        }
        check[now] = true;
        s.push(now);
        for(int i = 0;i<str.length();i++){
            if(check[i]) cout << str[i];
        }
        cout << "\n";
    }
}