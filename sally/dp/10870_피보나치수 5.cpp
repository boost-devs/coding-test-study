/*
# Tree
# Problem: 10870
# Memory: 2020KB
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
#include <deque>
#include <map>
#include <set>
using namespace std;

int N;
vector<int> v;

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> N;
    v.push_back(0);
    v.push_back(1);

    for(int i = 2; i <= N; i++){
        v.push_back(v[i - 1] + v[i - 2]);
    }

    if(N == 0) cout << "0\n";
    else cout << v[v.size()-1] << '\n';

    return 0;
}