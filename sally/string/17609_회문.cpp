/*
# String
# Problem: 17609
# Memory: 2500KB
# Time: 20ms
*/
#include <iostream>
#include <string.h>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <algorithm>
#include <cmath>
#include <deque>
using namespace std;

string str;
int T;

int func(string s, bool chance){
    int ret = 0;
    int len = s.size();
    int i = 0, j = len-1;
    bool success = true;
    while(i < j){
        if(s[i] != s[j]){
            if(i + 1 == j && chance) {
                chance = false;
                break;
            } else if(!chance){
                success = false;
                break;
            } else {
                chance = false;
                int tmp1 = func(s.substr(i, j - i), false);     // 좌 봐주기
                int tmp2 = func(s.substr(i + 1, j - i), false); // 우 봐주기

                if(tmp1 < tmp2) return tmp1;
                else return tmp2;
            }
        }
        i++; j--;
    }
    if(success && chance) ret = 0;
    else if(success && (!chance)) ret = 1;
    else ret = 2;

    return ret;
}


int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> T;
    while(T--){
        cin >> str;
        cout << func(str, true) << '\n';
    }

    return 0;
}