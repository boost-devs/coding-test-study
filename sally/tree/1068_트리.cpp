/*
# Tree
# Problem: 1068
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
using namespace std;

int N, result = 0, target;
int a, vlen, rt;
vector<int> v[51];

void traversal(int cur){
    int n_size = v[cur].size();
    bool is_leaf = true;
    for(int i = 0; i < n_size; i++){
        int nex = v[cur][i];
        if(nex != target){
            is_leaf = false;
            traversal(nex);
        }
    }
    if(is_leaf == true) result++;
}

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> N;
    for(int i = 0; i < N; i++){
        cin >> a;
        if(a == -1) rt = i;
        else v[a].push_back(i);
    }
    cin >>target;

    if(target != rt)
        traversal(rt);
    
    cout << result << '\n';

    return 0;
}
