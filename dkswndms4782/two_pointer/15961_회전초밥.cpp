#include <iostream>
#include <vector>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N,d,k,c,tmp; cin >> N >> d >> k >> c;
    vector<int>v;
    for(int i = 0;i<N;i++){
        cin >> tmp; v.push_back(tmp);
    }
    int check[4000];
    int count = 0;
    for(int i = 0;i<k;i++){
        check[v[i]]++;
        if(check[v[i]] > 1) count++;
    }
    int Min = count; int result = k-count; bool flag = false;
    if(check[c] == 0) result++;
    int start = 0; int end = k; 
    while(!flag){
        check[v[start]]--;
        if(check[v[start]] != 0) count--;
        check[v[end]]++;
        if(check[v[end]] > 1) count++;
        if(count <= Min){
            Min = count;
            if(check[c] == 0) result = max(result, k-Min+1);
            else result = max(result, k-Min);

        }
        start = (start + 1) % N;
        end = (end + 1) % N;
        if(start == 0) flag = true;
    }
    cout << result;

}