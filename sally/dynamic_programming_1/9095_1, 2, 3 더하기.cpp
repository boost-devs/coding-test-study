/*
# DP
# Problem: 9095
# Memory: 2020KB
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

int T;
int N;

int arr[12] ={0,};

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >>T;

    arr[1] = 1;
    arr[2] = 2;
    arr[3] = 4;

    for(int i = 4; i <=11; i++){
        arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3];
    }

    while(T--){
        cin >> N;
        cout << arr[N] << '\n';
    }

    return 0;
}