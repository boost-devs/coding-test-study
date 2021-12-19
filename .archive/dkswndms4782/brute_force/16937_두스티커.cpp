#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int H,W,R,C,N;
vector<pair<int,int>>sticker;

bool check(pair<int,int>a, pair<int,int>b){
    if(a.first + b.first <= H && max(a.second, b.second) <= W) return true;
    if(a.second + b.second <= W && max(a.first, b.first) <= H) return true;
    //a������
    if(a.second + b.first <= H && max(a.first, b.second) <= W) return true;
    if(a.first + b.second <= W && max(a.second, b.first) <= H) return true;
    //b������
    if(a.first + b.second <= H && max(a.second, b.first) <= W) return true;
    if(a.second + b.first <= W && max(a.first, b.second) <= H) return true;
    //�Ѵ� ������
    if(a.second + b.second <= H && max(a.first, b.first) <= W) return true;
    if(a.first + b.first <= W && max(a.second, b.second) <= H) return true;

    return false;
}

int main(){
    cin >> H >> W >> N;
    if(N == 1) {cout << 0; return 0;}
    for(int i = 0;i<N;i++){
        cin >> R >> C;
        sticker.push_back({R,C});
    }
    vector<int>v(N); v[0] = v[1] = -1;
    int result = -1;
    do{
        vector<int>now_sticker; 
        for(int i = 0;i<N;i++) if(v[i] == -1) now_sticker.push_back(i);
        if(check(sticker[now_sticker[0]], sticker[now_sticker[1]])) 
            result = max(result, sticker[now_sticker[0]].first*sticker[now_sticker[0]].second + sticker[now_sticker[1]].first*sticker[now_sticker[1]].second);
    }while(next_permutation(v.begin(), v.end()));
    if(result == -1) cout << 0;
    else cout << result;
}
// 2�� ���Ѱ� ���̿� ���ų� �۾ƾ���. ������ �ϳ��� max�� ���̿� ���ų� �۱�