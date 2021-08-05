#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
using namespace std;
char dna[4] = {'A','C', 'G', 'T'};
bool cmp(pair<char, int>a, pair<char, int>b){
    if(a.second > b.second) return true;
    if(a.second == b.second && a.first < b.first) return true;
    return false; 
}

int main(){
    int N,M; cin >> N >> M;
    vector<string>v; string tmp;
    for(int i = 0;i<N;i++){
        cin >> tmp;
        v.push_back(tmp);
    }
    string result_DNA = ""; int result_num = 0;
    for(int i = 0;i<M;i++){
        map<char, int>m;
        for(int j = 0;j<N;j++){
            m[v[j][i]]++;
        }
        vector<pair<char,int>>res;
        for(int j = 0;j<4;j++){
            res.push_back({dna[j], m[dna[j]]});
        }
        sort(res.begin(), res.end(), cmp);
        result_DNA += res[0].first;
        for(int i = 1;i<4;i++) result_num += res[i].second;
    }
    cout << result_DNA << "\n" << result_num;
}   