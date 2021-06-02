/*
# String
# Problem: 11365
# Memory: 2024KB
# Time: 0ms
*/
#include <iostream> 
#include <string.h>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>
#include <cmath>
#include <functional>
using namespace std;

string str;

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    getline(cin, str);
    while(str!="END"){
        // cout << "str: " <<str<< '\n';
        int str_len = str.size();
        for(int i = str_len -1; i >= 0; i--)
            cout << str[i];
        cout << '\n';
        cin.clear();
        getline(cin, str);
    }

    return 0;
}