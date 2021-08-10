#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int N,M;
int ch[31][31];
int result = -1;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> N >> M;
    for(int i = 0;i<N;i++) for(int j = 0;j<M;j++) cin >> ch[i][j];
    vector<int>v(M); v[0] = v[1] = v[2] = -1;  
    do{ 
        vector<int>brand;
        for(int i = 0;i<M;i++){
            if(v[i] == -1) brand.push_back(i);
        }
        int sum = 0;
        for(int i = 0;i<N;i++){
            int max_num = -1;
            for(int j = 0;j<3;j++){
                if(max_num < ch[i][brand[j]]) max_num = ch[i][brand[j]];
            }
            sum += max_num;
        }
        if(sum > result) result = sum;
    }while(next_permutation(v.begin(), v.end()));
    cout << result;
}