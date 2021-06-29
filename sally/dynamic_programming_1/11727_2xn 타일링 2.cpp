/*
# DP
# Problem: 11727
# Memory: 2024KB
# Time: 0ms
*/
#include <iostream>
#include <string>
#include <string.h>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <cmath>
using namespace std;

int N;
int arr[1001] = {0};

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> N;
    arr[1] = 1;
    arr[2] = 3;
    for(int i = 3; i <= N; i++)
        arr[i] = (arr[i - 1] + (arr[i - 2] * 2)) % 10007;

    cout << arr[N];

    return 0;
}