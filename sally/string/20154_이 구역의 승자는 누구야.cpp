/*
# String
# Problem: 20154
# Memory: 7328KB
# Time: 16ms
*/
#include <iostream>
#include <string.h>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>
#include <cmath>
#include <functional>
using namespace std;

string str;
int N;
int num_line[26] = {3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1};
int cur = 0;
queue<int> q;

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    // input
    cin >> str;
    N = str.size();
    for(int i = 0; i < N; i++) q.push(num_line[str[i] - 'A']);

    
    while(!q.empty()){
        int q_size = q.size();
        if(q_size == 1) break;
        if(q_size % 2 == 1) {
            q.push(0);
            q_size++;
        }
        for(int t = 0; t < q_size; t++){
            if(cur == 0) {
                cur = q.front();
                q.pop();
            } else {
                q.push((q.front() + cur) % 10);
                q.pop();
                cur = 0;
            }
        }
    }
    
    if(q.front() % 2 == 0) cout << "You're the winner?\n";
    else cout << "I'm a winner!\n";

    return 0;
}
