/*
# DP
# Problem: 1912
# Memory: 2412KB
# Time: 8ms
*/
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    
    int N; cin >> N;
    vector<int> arr(N, 0);
    for(int i = 0; i < N; i++) cin >> arr[i];

    for(int i = N-2; i >= 0; i--)
        arr[i] = max(arr[i], arr[i] + arr[i+1]);

    int ret = arr[0];
    for(auto i : arr)
       ret = max(ret, i);

    cout <<ret;

    return 0;
}