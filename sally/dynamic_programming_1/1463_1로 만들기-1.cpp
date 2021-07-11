/*
# DP
# Problem: 1463
# Memory: 7828KB
# Time: 24ms
*/
#include <iostream>
#include <string>
#include <string.h>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <cmath>
using namespace std;

int N;
int arr[1000001] = {0,};
bool visited[1000001] = {false,};
queue<int> q;

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    cin >> N;
    for(int i = 0; i <= N; i++) arr[i] = N;

    arr[1] = 0;
    q.push(1);

    while(!q.empty()){
        int cur = q.front();
        q.pop();

        if (cur * 3 <= N && !visited[cur*3]){
            arr[cur * 3] = min(arr[cur * 3], arr[cur] + 1);
            q.push(cur*3);
            visited[cur*3] = true;
            if (cur * 3 == N)
                break;
        }

        if (cur * 2 <= N && !visited[cur * 2])
        {
            arr[cur * 2] = min(arr[cur * 2], arr[cur] + 1);
            q.push(cur*2);
            visited[cur * 2] = true;
            if (cur * 2 == N)
                break;
        }

        if (cur + 1 <= N && !visited[cur + 1]) {
            arr[cur + 1] = min(arr[cur + 1], arr[cur] + 1);
            q.push(cur+1);
            visited[cur + 1] = true;
            if (cur + 1 == N)
                break;
        }
    }

    cout << arr[N];
    
    return 0;
}