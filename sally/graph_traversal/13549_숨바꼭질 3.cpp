/*
Graph Traversal - Priority Queue, BFS
# Problem: 13549
# Memory: 2628KB
# Time: 4ms
*/
#include <iostream> 
#include <string.h>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

#define MAX_ 100000

int N, K;
bool visit[100001] = {false};
priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> q;
int result = 0;
int nex[3] = {0, };

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    // input
    cin >> N >> K;
    visit[N] = true;
    q.push({0, N});
    
    while(!q.empty()){
        // cur, pop
        int cur_time = q.top().first;
        int cur_loc = q.top().second;
        q.pop();

        // find
        if(cur_loc == K) {
            result = cur_time;
            break;
        }

        nex[0] = cur_loc * 2;
        nex[1] = cur_loc + 1;
        nex[2] = cur_loc - 1;

        for(int i = 0; i < 3; i++){
            if(0 <= nex[i] && nex[i] <= MAX_)
                if(visit[nex[i]] == false){
                    visit[nex[i]] = true;
                    if(i == 0){ // 순간이동
                        q.push({cur_time, nex[i]});
                    }else{ // 일반이동
                        q.push({cur_time+1, nex[i]});
                    }
                }
        }
    }

    cout << result << '\n';

    return 0;
}
