#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

bool check(int N){
    int one = N%10;
    int two = (N/10)%10;
    int three = N/100;
    if(one == 0 || two == 0) return false;
    if(one == two || two == three || three == one) return false;
    return true;
}

pair<int,int> func(int a,int b){
    int strike = 0; int ball = 0;
    for(int i = 0;i<3;i++){
        for(int j = 0;j<3;j++){
            int tmp_a = (a / int(pow(10, i))) % 10;
            int tmp_b = (b / int(pow(10, j))) % 10;
            if(i == j && tmp_a == tmp_b) strike++;
            else if(i != j && tmp_a == tmp_b) ball++;
        }
    }
    return {strike, ball};
}

int main(){
    int count = 0; vector<int>v; int N; cin >> N;
    for(int i = 111; i<1000;i++) if(check(i)) v.push_back(i);
    int question[101][3];
    for(int i = 0;i<N;i++) cin >> question[i][0] >> question[i][1] >> question[i][2];
    for(int i = 0;i<v.size();i++){
        int flag = true;
        for(int j = 0;j<N;j++){
            pair<int,int>tmp = func(v[i], question[j][0]);
            if(tmp.first != question[j][1] || tmp.second != question[j][2]){flag = false; break;}
        }
        if(flag) count++;
    }
    cout << count;
}