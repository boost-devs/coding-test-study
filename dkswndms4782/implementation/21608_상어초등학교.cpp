#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct STUDENT{
    int num;
    int Friend[4];
};
struct seat{
    int x; int y;
    int empty;
    int near;
};
vector<STUDENT>order;
STUDENT arr[450];
int now_seat[25][25];
int dx[4] = {0,0,1,-1};
int dy[4] = {1,-1,0,0};

bool cmp(seat a, seat b){
    if(a.near > b.near) return true;
    if(a.near == b.near && a.empty > b.empty) return true;
    if(a.near == b.near && a.empty == b.empty && a.x < b.x) return true;
    if(a.near == b.near && a.empty == b.empty && a.x == b.x && a.y < b.y) return true;
    return false;
}



int main(){
    int N; cin >> N;
    int a,b,c,d,e;
    int tmp = N*N;
    while(tmp--){
        cin >> a >> b >> c >> d >> e;
        order.push_back({a,{b,c,d,e}});
        arr[a].num = a;
        arr[a].Friend[0] = b;
        arr[a].Friend[1] = c;
        arr[a].Friend[2] = d;
        arr[a].Friend[3] = e;
    }
    for(int k = 0;k<order.size();k++){
        vector<seat>s;
        int now_num = order[k].num;
        for(int i = 0;i<N;i++){
            for(int j = 0;j<N;j++){
                if(now_seat[i][j] != 0) continue;
                int friend_count = 0;
                int empty_count = 0;
                for(int t = 0;t < 4;t++){
                    int t1 = i + dx[t];
                    int t2 = j + dy[t];
                    if(t1 < 0 || t2 < 0 || t1 >= N || t2 >= N) continue;
                    if(now_seat[t1][t2] == 0) empty_count++;
                    else{
                        for(int p = 0;p<4;p++){
                            int friend_num = order[k].Friend[p];
                            if(now_seat[t1][t2] == friend_num){
                                friend_count++;
                                break;
                            }
                        }
                    }
                }
                s.push_back({i,j,empty_count,friend_count});
            }
        }
        sort(s.begin(), s.end(), cmp);
        int tmp_x = s[0].x;
        int tmp_y = s[0].y;
        now_seat[tmp_x][tmp_y] = now_num;
    }  
    int result = 0;
    for(int i = 0;i<N;i++){
        for(int j = 0;j<N;j++){
            int now_num = now_seat[i][j];
            int friend_count = 0;
            for(int k = 0;k<4;k++){
                int t1 = i + dx[k];
                int t2 = j + dy[k];
                if(t1 < 0 || t2 < 0 || t1 >= N || t2 >= N) continue;
                for(int p = 0;p<4;p++){
                    int friend_num = arr[now_num].Friend[p];
                    if(now_seat[t1][t2] == friend_num){
                        friend_count++;
                        break;
                    }
                }
            }
            if(friend_count == 1) result += 1;
            else if(friend_count == 2) result += 10;
            else if(friend_count == 3) result += 100;
            else if(friend_count == 4) result += 1000;
        }
    }
    cout << result;
}   