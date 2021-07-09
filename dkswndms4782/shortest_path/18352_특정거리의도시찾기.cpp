#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int main(){
    vector<int>v[300001];
    int N,M,K,X,A,B;
    cin >> N >> M >> K >> X;
    for(int i = 0;i<M;i++){
        cin >> A >> B;
        v[A].push_back(B);
    }
    queue<pair<int,int>>pq;
    bool visit[300001];
    pq.push(make_pair(X,0));
    visit[X] = true;
    vector<int>result;
    while(!pq.empty()){
        int tmpCity = pq.front().first;
        int tmpCount = pq.front().second;
        pq.pop();
        if(tmpCount == K)
            result.push_back(tmpCity);
        for(int i = 0;i<v[tmpCity].size();i++){
            if(!visit[v[tmpCity][i]]){
                pq.push(make_pair(v[tmpCity][i], tmpCount + 1));
                visit[v[tmpCity][i]] = true;
            }
        }
    }
    sort(result.begin(), result.end());
    if(result.size() == 0) cout << -1;
    else{
        for(int i = 0;i<result.size();i++)
            cout << result[i] << "\n";
    }
}