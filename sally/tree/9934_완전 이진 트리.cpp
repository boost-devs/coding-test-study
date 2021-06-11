/*
# Tree
# Problem: 9934
# Memory: 2208KB
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
using namespace std;

int K, a, total_len;
queue<pair<int, int>> q;
vector<int> v;


int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> K;
    v.push_back(0);
    int N = pow(2, K) -1;
    for(int i = 0; i < N; i++){
        cin >> a;
        v.push_back(a);
    }
    total_len = v.size();

    int start_ = (pow(2, K-1));
    int step_ = start_;
    q.push({start_, step_});
    K--;
    cout << v[start_] << '\n';
    v[start_] = 0;

    while(K--){
        int q_size = q.size();
        for(int t = 0; t < q_size; t++){
            int cur = q.front().first;
            int lr = q.front().second;
            q.pop();

            int target1 = cur - (lr / 2);
            int target2 = cur + (lr / 2);
            if(1 <= target1 && target1 < total_len){
                if(v[target1]!=0){
                    q.push({target1, lr / 2});
                    cout << v[target1] << ' ';
                    v[target1] = 0;
                }
            }

            if(1 <= target2 && target2 < total_len){
                if(v[target2]!=0){
                    q.push({target2, lr / 2});
                    cout << v[target2] << ' ';
                    v[target2] = 0;
                }
            }

        }
        cout << '\n';
    }


    return 0;
}