/*
Graph Traversal - string
# Problem: 11720
# Memory: 2024KB
# Time: 0ms
*/
#include <iostream> 
#include <string.h>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

int N;
int result = 0;
string str;

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> N >> str;
    for(int i = 0; i <N; i++){
        result += (str[i] - '0');
    }

    cout << result;

    return 0;
}