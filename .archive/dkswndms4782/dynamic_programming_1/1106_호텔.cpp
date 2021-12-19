#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int customer[2001] = {0,};
    pair<int,int>city[21];
    int C,N, a,b; cin >> C >> N;
    for(int i = 0;i<N;i++){
        cin >> a >> b;
        city[i] = make_pair(a,b);
        if(customer[b] != 0) customer[b] = min(a, customer[b]);
        else customer[b] = a;
    }
    for(int i = 1;i<=C;i++){
        if(customer[i] != 0){
            for(int j = 0;j<N;j++){
                if(customer[i + city[j].second] != 0) 
                    customer[i + city[j].second] = min(customer[i + city[j].second], customer[i] + city[j].first);
                else
                    customer[i + city[j].second] = customer[i] + city[j].first;
            }
        }
    }
    int m = 1000000001;
    for(int i = C;i<= (C + 100);i++) if(customer[i]!=0) m = min(m, customer[i]);
    cout << m;
}