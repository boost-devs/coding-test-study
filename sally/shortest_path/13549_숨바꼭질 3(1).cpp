/*
# DP
# Problem: 13549
# Memory: 2632KB
# Time: 4ms
*/
#include <iostream>
#include <cmath>
#include <vector>
#include <queue>
using namespace std;

#define MAX 100001
#define my_pair pair<int, int>

int N, K;
int result = 0;
priority_queue<my_pair, vector<my_pair>, greater<my_pair>> q;
bool visit[MAX] = {false,};

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    // input
    cin >> N >> K;

    // init
    visit[N] = true; 
    q.push({0, N}); // val, ind

    // dijkstra
    while(!q.empty()){
        int cur = q.top().second;
        int cur_day = q.top().first;
        q.pop();

        // end condition
        if(cur == K) {
            result = cur_day;
            break;
        }

        // important !!! sequence(*2 -> +1 -> -1)
        int target = cur * 2;
        if (0 <= target && target < MAX)
            if (!visit[target])
            {
                visit[target] = true;
                q.push({cur_day, target});
            }
        target = cur + 1;
        if (0 <= target && target < MAX)
            if(!visit[target]) {
                visit[target] = true;
                q.push({cur_day + 1, target});
            }

        target = cur - 1;
        if (0 <= target && target < MAX)
            if (!visit[target]){
                visit[target] = true;
                q.push({cur_day + 1, target});
            }

        
    }

    cout << result;

    return 0;
}