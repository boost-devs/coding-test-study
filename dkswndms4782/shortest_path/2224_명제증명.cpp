#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

vector<pair<char, char>>result;
void dfs(char ori,char next, vector<char>v[], bool check[]){
    for(int i= 0;i<v[next].size();i++){
        if(check[v[next][i]] == false) {
            if(ori != v[next][i])
                result.push_back({ori, v[next][i]});
            check[v[next][i]] = true;
            dfs(ori,v[next][i], v, check);
        }
    }
}

bool compare(pair<char,char>a, pair<char, char>b){
    if(a.first < b.first) return true;
    else if(a.first == b.first && a.second < b.second) return true;
    return false;
}

int main(){
    int N; cin >> N;
    char A,a,b,B;
    vector<char>v[200];
    bool check[200] = {false,};
    while(N--){
        cin >> A >> a >> b >> B;
        v[int(A)].push_back(B);
    }
    for(int i = 65;i<=90;i++){
        if(v[i].size() != 0){
           fill(check, check+200, false);
           dfs(i,i, v, check);
        }
    }
    for(int i = 97;i<=122;i++){
        if(v[i].size() != 0){
           fill(check, check+200, false);
           dfs(i,i, v, check);
        }
    }
    sort(result.begin(), result.end(), compare);
    cout << result.size() << "\n";
    for(int i = 0;i<result.size();i++){
        cout << result[i].first << " " << a << b << " " << result[i].second << "\n";
    }
}
