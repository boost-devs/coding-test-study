/*
# DP
# Problem: 1010
# Memory: 2028KB
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

int T, N, M;
long long arr[31][31] = {0};

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> T;
    while(T--){
        cin >> N >> M;
        arr[1][1] = 1;
        for(int i = 1; i <= M; i++)
            arr[1][i] = i;
        for (int i = 1; i <= N; i++)
            arr[i][i] = 1;
        for(int i = 2; i <= N; i++){
            for(int j = i + 1; j <= M; j++){
                arr[i][j] = arr[i-1][j-1] + arr[i][j-1];
            }
        }
        cout << arr[N][M] <<'\n';
    }

    return 0;
}