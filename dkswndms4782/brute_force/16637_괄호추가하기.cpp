#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(){
    int N; cin >> N;
    string s; cin >> s;
    vector<pair<int,int>>a(N); // first : num, second : 0,1,2,3(각 수,+,-,* 의미)
    // 3,0이면 현재 숫자이며 값은 3 // 0,1이면 현재 연산자이며 +를 의미
    for(int i= 0;i<N;i++){
        if(i%2 == 0) a[i] = {s[i]-'0', 0};
        else {
            int tmp = 1;
            if(s[i] == '-') tmp = 2;
            else if(s[i] == '*') tmp = 3;
            a[i] = {0,tmp};
        }
    }
    int operator_cnt = (N-1)/2;
    int result = -1e9;
    for(int i = 0;i<(1<<operator_cnt);i++){
        bool flag = true;
        for(int j = 0;j<operator_cnt-1;j++) if((i&(1<<j)) > 0 && (i&(1<<(j+1))) > 0) flag = false;
        if(!flag) continue;
        vector<pair<int,int>>b(a);
        for(int j = 0;j<operator_cnt;j++){
            if((i&(1<<j)) > 0){
                int k = 2*j + 1;
                if(b[k].second == 1){
                    b[k-1].first += b[k+1].first;
                    b[k+1].first = 0;
                }
                else if(b[k].second == 2){
                    b[k-1].first -= b[k+1].first;
                    b[k].second = 1;
                    b[k+1].first = 0;
                }
                else if(b[k].second == 3){
                    b[k-1].first *= b[k+1].first;
                    b[k].second = 1;
                    b[k+1].first = 0;
                }
            }
        }
        int tmp_result = b[0].first;
        for(int j = 0;j<operator_cnt;j++){
            int k = 2*j+1;
            if(b[k].second == 1) tmp_result += b[k+1].first;
            else if(b[k].second == 2) tmp_result -= b[k+1].first;
            else if(b[k].second == 3) tmp_result *= b[k+1].first;
        }
        if(result < tmp_result) result = tmp_result;
    }
    cout << result;
}
