/*
# DP
# Problem: 2224
# Memory: 2028KB
# Time: 0ms
*/
#include <iostream>
#include <vector>
#include <cmath>
#include <queue>
#include <algorithm>
#include <string>
#include <string.h>
using namespace std;

int N, result = 0;;
bool arr[58][58] = {false, };

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> N;
    for(int i = 0; i < N; i++) {
        char a, b; string c;
        cin >> a >> c >> b;
        arr[a-'A'][b-'A'] = true;
    }

    for (int k = 0; k < 58; k++)
        for (int i = 0; i < 58; i++)
            for (int j = 0; j < 58; j++)
                if (arr[i][k] && arr[k][j])
                    arr[i][j] = true;

    for (int i = 0; i < 58; i++)
        for (int j = 0; j < 58; j++)
            if(i != j && arr[i][j] == true) result++;
    cout << result << '\n';
    
    for(int i = 0; i < 58; i++)
        for (int j = 0; j < 58; j++)
            if (arr[i][j] && (i != j))
                cout << char(i+65) << " => " << char(j+65) << '\n';
    return 0;
}