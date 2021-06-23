/*
# DP
# Problem: 17626
# Memory: 2216KB
# Time: 8ms
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
int arr[50001] = {0,};
vector<int> cand;

int get_min(int n){
    int result = 4;
    if(n % 2 == 0 && arr[n/2] < 2)
        result = arr[n/2] * 2;

    int las = n/2;
    // for(int i = 1; i < las; i++){
    for(auto i: cand){
        if(i>n) break;
        result = min(result, arr[i] + arr[n - i]);
    }

    return result;
}

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> N;
    arr[1] = 1;
    for(int i = 1; i < 300; i++)
        if(i*i <= 50000) {
            cand.push_back(i*i);
            arr[i*i] = 1;
        }

    for(int i = 2; i <= N; i++){
        if(arr[i] == 0)
            arr[i] = get_min(i);
    }
        
        

    cout << arr[N];


    return 0;
}