/*
# String
# Problem: 10798
# Memory: 2024KB
# Time: 0ms
*/
#include <iostream> 
#include <string.h>
#include <string>
using namespace std;

string str;
char cmap[5][20] = {'.', };

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    for(int i = 0; i < 5; i++){
        for(int j = 0; j < 20; j++) cmap[i][j] = '.';
        cin >> str;
        int str_len = str.size();
        for(int j = 0; j < str_len; j++)
            cmap[i][j] = str[j];
    }

    for(int i = 0; i < 20; i++)
        for(int j = 0; j < 5; j++)
            if (cmap[j][i] != '.' && cmap[j][i] != ' ')
                cout << cmap[j][i];

    return 0;
}