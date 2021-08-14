#include <iostream>
using namespace std;
#define MAX 100000000

int N; int map[11][11]; int min_num = MAX;
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};
bool visit[11][11] = {false,};
bool check(int a, int b){
    if(visit[a][b]) return false;
    for(int i = 0;i<4;i++){
        int tmp_x = a + dx[i];
        int tmp_y = b + dy[i];
        if(tmp_x >= N || tmp_y >= N || tmp_x < 0 || tmp_y < 0||visit[tmp_x][tmp_y]) return false;
        
    }
    return true;
}

void dfs(int cnt, int sum){
    if(cnt == 3) {if(min_num > sum) min_num = sum; return;}
    for(int i = 0; i<N;i++){
        for(int j = 0;j<N;j++){
            if(!check(i,j)) continue;
            int now = map[i][j];
            visit[i][j] = true;
            for(int d = 0;d<4;d++){
                int t1 = i + dx[d];
                int t2 = j + dy[d];
                visit[t1][t2] = true;
                now += map[t1][t2];
            }
            dfs(cnt + 1, sum+now);

            visit[i][j] = false;
            for(int d = 0;d<4;d++){
                int t1 = i + dx[d];
                int t2 = j + dy[d];
                visit[t1][t2] = false;
            }
        }
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> N;
    for(int i = 0;i<N;i++) for(int j = 0;j<N;j++) cin >> map[i][j];
    dfs(0,0);
    cout << min_num;
}