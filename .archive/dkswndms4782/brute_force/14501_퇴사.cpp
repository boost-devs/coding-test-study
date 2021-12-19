#include <iostream>
#include <vector>
using namespace std;

int N; int T,P; vector<pair<int,int>>v; int result = -1;
void func(int now, int sum){
    if(now > N) return;
    if(now == N) {if(result < sum) {result = sum;} return;}
    func(now + v[now].first, sum + v[now].second);
    func(now + 1, sum);
}

int main(){
    cin >> N; int t,p;
    for(int i = 0;i<N;i++){
        cin >> t >> p;
        v.push_back({t,p});
    }
    func(0,0);
    cout << result;
}