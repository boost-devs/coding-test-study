/*
# DP
# Problem: 9655
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

string str[2] = {"SK", "CY"}; // false, true
bool winner = false;
int N;

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> N;
    
    int mok = N / 3;
    int namo = N % 3;

    if(mok % 2 == 1) winner = false;
    else winner = true;

    if(namo % 2 == 0) cout << str[winner];
    else if(namo == 1) cout << str[!winner];

    return 0;
}