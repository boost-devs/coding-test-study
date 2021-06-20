/*
# String
# Problem: 9342
# Memory: 2028KB
# Time: 0ms
*/
#include <iostream>
#include <string.h>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

int T;
string str;
vector<char> v;
vector<string> target;

string target_ch[6] = {"A", "B", "C", "D", "E", "F"};

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    target.push_back("AFC");
    for(int i = 0; i < 6; i++)
        for(int j = 0; j <6; j++){
            if(i==0 || j==2) continue;
            target.push_back(target_ch[i] + "AFC" + target_ch[j]);
        }

    for(int i = 1; i < 6; i++)
        target.push_back(target_ch[i] + "AFC");
    for (int i = 0; i < 6; i++)
        if(i != 2)
            target.push_back("AFC" + target_ch[i]);

    cin >> T;
    while(T--){
        bool success = false;
        cin >> str;
        v.clear();
        for(auto s: str)
            v.push_back(s);
        v.erase(unique(v.begin(), v.end()),v.end());
        
        string s;
        for(auto i: v)
            s += i;
        for(auto j: target)
            if(s == j) success = true;
        
        if(success == true) cout << "Infected!\n";
        else cout << "Good\n";
    }


    return 0;
}