/*
# Tree
# Problem: 14675
# Memory: 2412KB
# Time: 32ms
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

int N, q, a, b, t , k;
int v[100001] = {0, };

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> N;
    for(int i = 0; i < N-1; i++){
        cin >> a >> b;
        v[a]++;
        v[b]++;
    }

    cin >> q;
    while(q--){
        cin >> t >> k;
        if(t == 2){
            cout <<"yes\n";
            continue;
        }
        if(v[k] >= 2) cout << "yes\n";
        else cout <<"no\n";
    }

    return 0;
}