#include <iostream>
#include <vector>
using namespace std;

int result[101][101] = {0,};

void dfs(int ori,int next, vector<int>v[], bool check[]){
    for(int i= 0;i<v[next].size();i++){
        if(check[v[next][i]] == false) {
            result[ori][v[next][i]] = 1; 
            check[v[next][i]] = true;
            dfs(ori,v[next][i], v, check);
        }
    }
}

int main(){
   ios_base::sync_with_stdio(false);
   cin.tie(NULL);
   int  N; cin >> N;
   vector<int>v[101]; int tmp;
   for(int i = 0;i<N;i++){
       for(int j = 0;j<N;j++){
           cin >> tmp;
           if(tmp == 1) v[i].push_back(j);
       }
    }
    bool check[101] = {false,};
    for(int i = 0;i<N;i++){
        fill(check, check+101, false);
        dfs(i,i, v, check);
    }
    for(int i = 0;i<N;i++){
        for(int j = 0;j<N;j++){
            cout << result[i][j] << " ";
        }
        cout << "\n";
    }
    
}