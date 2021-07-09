/*
# DP
# Problem: 11403
# Memory: 2032KB
# Time: 0ms
*/
#include <iostream>
#include <vector>
#include <cmath>
#include <queue>
#include <algorithm>
using namespace std;

int N;
bool arr[101][101] = {false,};

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> N;
    for(int i = 0; i < N; i++)
        for(int j = 0; j < N; j++) cin >> arr[i][j];
        
    for(int i = 0; i < N; i++)
        for(int j = 0; j < N; j++)
            for (int k = 0; k < N; k++)
                if (arr[i][k] && arr[k][j])
                    arr[i][j] = true;

    for(int i = 0; i < N; i++){
        for (int j = 0; j < N; j++) cout << arr[i][j] << ' ';
        cout << '\n';
    }
    
    return 0;
}