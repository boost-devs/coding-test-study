#include <iostream>
using namespace std;

char coin[3][3];
pair<int,int> arr[8][3] = {{{0,0},{0,1},{0,2}},{{1,0},{1,1},{1,2}},{{2,0},{2,1},{2,2}},
                            {{0,0},{1,0},{2,0}},{{0,1},{1,1},{2,1}},{{0,2},{1,2},{2,2}},
                            {{0,0},{1,1},{2,2}},{{2,0},{1,1},{0,2}}};

int main(){
    int T; cin >> T;
    for(int i = 0;i<T;i++){
        for(int j = 0;j<3;j++) for(int k = 0;k<3;k++) cin >> coin[j][k];
        int result = 9;
        for(int j = 0;j<(1<<8);j++){
            int cnt = 0; char tmp[3][3];
            for(int a = 0;a<3;a++) for(int b = 0;b < 3;b++) tmp[a][b] = coin[a][b];
            for(int k = 0;k<8;k++){
                if(j & (1<<k)){
                    cnt++;
                    for(int a = 0;a<3;a++){
                        if(tmp[arr[k][a].first][arr[k][a].second] == 'T') tmp[arr[k][a].first][arr[k][a].second] = 'H';
                        else tmp[arr[k][a].first][arr[k][a].second] = 'T';
                    }
                }
            }
            char now = tmp[0][0]; bool flag = true;
            for(int a = 0;a<3;a++) for(int b = 0;b<3;b++) if(now != tmp[a][b]) flag = false;
            if(flag && result > cnt) result = cnt;
        }
        if(result == 9) cout << -1 << "\n";
        else cout << result << "\n";
    }
}