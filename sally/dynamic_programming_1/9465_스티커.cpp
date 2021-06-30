/*
# DP
# Problem: 9465
# Memory: 2800KB
# Time: 80ms
*/
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int T, N, ret;
int arr[2][100001] = {0,};

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    
    cin >> T;
    while(T--){
        cin >> N;
        for(int i = 0; i <N; i++) cin >> arr[0][i];
        for(int i = 0; i <N; i++) cin >> arr[1][i];

        ret = max(arr[0][0], arr[1][0]);
        for(int i = 1; i <N; i++){
            arr[0][i] = max(arr[0][i-1], arr[1][i-1] + arr[0][i]);
            arr[1][i] = max(arr[1][i-1], arr[0][i-1] + arr[1][i]);
            ret = max(ret, max(arr[0][i], arr[1][i]));
        }
        cout << ret << '\n';
    }

    return 0;
}