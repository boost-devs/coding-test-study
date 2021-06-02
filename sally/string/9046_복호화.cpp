/*
# String
# Problem: 9046
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

int N;
string str;
int num[30] = {0, };
vector< pair<int, int> > v;

bool compare(pair<int, int>i , pair<int, int> j){
    return i.first > j.first;
}


int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> N;
    cin.ignore();

    for(int i = 0; i < N; i++){
        v.clear();
        memset(num, 0, sizeof(num));
        getline(cin, str);

        int str_len = str.size();
        if(str_len == 1) {
            cout << str << '\n';
            continue;
        }
        for(int j = 0; j < str_len; j++){
            if(str[j] == ' ') continue;
            num[str[j] - 'a']++;
        }

        for(int j = 0; j < 30; j++)
            v.push_back({num[j], j}); // num, alphabet
            
        sort(v.begin(), v.end(), compare);

        if(v[0].first == v[1].first) cout << "?\n";
        else cout << char(v[0].second + 'a') << '\n';
    }

    return 0;
}