/*
# DP
# Problem: 11265
# Memory: 3000KB
# Time: 40ms
*/
#include <iostream>
#include <cmath>
#include <string>
#include <string.h>
using namespace std;

#define success "Enjoy other party"
#define fail "Stay here"

int N, M;
int A, B, C;
int arr[501][501];

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> N >> M;
    for(int i = 1; i <= N; i++)
        for(int j = 1; j <= N; j++)
            cin >> arr[i][j];

    for (int k = 1; k <= N; k++)
        for (int i = 1; i <= N; i++)
            for (int j = 1; j <= N; j++)
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j]);

    while(M--){
        cin >> A >> B >> C;
        if(arr[A][B] <= C) cout << success << '\n';
        else cout << fail << '\n';
    }

    return 0;
}