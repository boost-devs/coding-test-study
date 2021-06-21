/*
# Tree
# Problem: 2839
# Memory: 2040KB
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

int target;
int sugar[5001] = {0};

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    
    cin >> target;

    sugar[3] = 1;
    sugar[5] = 1;

    for(int i = 6; i <= target; i++){
        if (sugar[i - 3] != 0 && sugar[i - 5] != 0)
            sugar[i] = min(sugar[i - 3], sugar[i - 5]) + 1;
        else if (sugar[i - 3] != 0 && sugar[i - 5] == 0)
            sugar[i] = sugar[i - 3] + 1;
        else if (sugar[i - 3] == 0 && sugar[i - 5] != 0)
            sugar[i] = sugar[i - 5] + 1;
    }

    if (sugar[target] != 0)
        cout << sugar[target] << '\n';
    else cout << "-1\n";
    
    return 0;
}