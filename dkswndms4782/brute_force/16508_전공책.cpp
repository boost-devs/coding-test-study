#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
using namespace std;

string T; int N,C; 
string book[51];
int price[51];
map<char,int>b;
int result = 160000000;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> T >> N;
    for(int i = 0;i<T.size();i++) b[T[i]] += 1;
    for(int i = 0;i<N;i++) cin >> price[i] >> book[i];
    vector<int>v(N);
    for(int a = 0;a<N;a++){
        v[a] = -1;
        do{
            map<char,int>tmp; int sum = 0;
            for(int i = 0;i<N;i++) {
                if(v[i] == -1) {
                    for(int j = 0;j<book[i].size();j++) tmp[book[i][j]]++; 
                    sum += price[i];
                }
            } 
            bool flag = true;
            for(int i = 0;i<T.size();i++){
                if(b[T[i]] > tmp[T[i]]) {flag = false; break;}
            }
            if(flag && result > sum) result = sum;
        }while(next_permutation(v.begin(), v.end()));
    }
    if(result == 160000000) cout << -1;
    else cout << result;
}