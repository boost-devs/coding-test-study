/*
# String
# Problem: 1181
# Memory: 5056KB
# Time: 24ms
*/
#include <iostream>
#include <string.h>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

int N;
string str;
vector<pair<int, string>> v;


int main(void) {

    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> N;
    for(int i = 0; i < N; i++){
        cin >> str;
        v.push_back({str.size(), str});
    }
    v.push_back({51, " "});

    sort(v.begin(), v.end());

    for(int i = 0; i < N; i++){
        if(v[i].second != v[i+1].second)
            cout << v[i].second << '\n';
    }
        

    return 0;
}