/*
# DP
# Problem: 1753
# Memory: 9184KB
# Time: 100ms
*/
#include <iostream>
#include <cmath>
#include <string>
#include <string.h>
#include <queue>
#include <algorithm>
#include <vector>
using namespace std;

#define INF 1e9
#define MAX 20001
#define my_pair pair<int, int> // pair<int, pair<int, int> >

int V, E, K;
int result[MAX] = {0,};

vector<pair<int, int>> arr[MAX]; // next, weight
priority_queue<my_pair, vector<my_pair>, greater<my_pair>> pq; // weight, {u, v}

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    // init
    cin >> V >> E >> K;
    for(int i = 0; i < E; i++){
        int u, v, w; cin >> u >> v >> w;
        arr[u].push_back({v, w});
    }
    for(int i = 1; i <= V; i++) result[i] = INF;

    // start node
    result[K] = 0;
    pq.push({0, K});

    while(!pq.empty()){
        int cur = pq.top().second;
        int cur_w = pq.top().first;
        pq.pop();

        if(cur_w > result[cur]) continue;

        for(auto i: arr[cur]){
            int next = i.first;
            int next_w = cur_w + i.second;

            if(result[next] > next_w) {
                result[next] = next_w;
                pq.push({next_w, next});
            }
        }
    }
    
    // print
    for(int i = 1; i <= V; i++)
        if(result[i] == INF) cout << "INF\n";
        else cout << result[i] <<'\n'; 

    return 0;
}