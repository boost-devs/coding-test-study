#include <iostream>
#include <algorithm>
using namespace std;
#define INF (int)1e9
int N,M,A,B;
int city[101][101], dist[101][101];

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> M;
    for(int i = 0;i<M;i++){
        cin >> A >> B;
        city[A][B] = city[B][A] = 1;
    }
    for(int i = 1;i<=N;i++){
        for(int j = 1;j<=N;j++){
            if(i == j) continue;
            else if (city[i][j]) dist[i][j] = 1;
            else dist[i][j] = INF;
        }
    }
    for(int k = 1;k<=N;k++){
        for(int i = 1;i<=N;i++){
            for(int j = 1;j<=N;j++){
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }
    pair<int,int>result; int Min = INF;
    for(int i = 1;i<=N;i++){
        for(int j = i+1;j<=N;j++){
            int Sum = 0;
            for(int k = 1;k<=N;k++) Sum += min(dist[i][k], dist[j][k]);
            if(Min > Sum){
                result = {i,j};
                Min = Sum;
            }
        }
    }
    cout << result.first << " " << result.second << " " << Min * 2;
}