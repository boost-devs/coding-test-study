#include <iostream>
#include <algorithm>
using namespace std;
int INF = 10000000;

int main(){
    int N,M,A,B,C; cin >> N >> M;
    int time[501][501];
    for(int i = 0;i<N;i++) for(int j = 0;j<N;j++) cin >> time[i][j];
    // k : 거쳐가는 정점, i : 출발 정점, j : 도착 정점
    for(int k=0;k<N;k++) for(int i=0;i<N;i++) for(int j=0;j<N;j++) time[i][j] = min(time[i][j], time[i][k] + time[k][j]);
    while(M--){
        cin >> A >> B >> C;
        if(time[A-1][B-1] <= C) cout << "Enjoy other party\n";
        else cout << "Stay here\n";
    }
}