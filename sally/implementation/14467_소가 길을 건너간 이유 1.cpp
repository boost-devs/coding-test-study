/*
# Implementation
# Problem: 14467
# Memory: 2020KB
# Time: 0ms
*/
#include <iostream>
using namespace std;

int N, num, dir, ret = 0;
int arr[11] = {0,};

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> N;
    for(int i = 1; i <= 10; i++) arr[i] = -1;
    for(int i = 0; i < N; i++){
        cin >> num >> dir;
        if(arr[num] == -1) {
            arr[num] = dir;
            continue;
        }
        if(arr[num] != dir) {
            arr[num] = dir;
            ret++;
        }
    }
    cout << ret;
    return 0;
}