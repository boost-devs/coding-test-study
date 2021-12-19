#include <iostream>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N,K; cin >> N >> K;
    int count[100001] = {0,}; int max_length = 0;
    int num[200001]; int start = 0; int end = 0;
    for(int i = 0;i<N;i++) cin >> num[i];
    while(end != N){
        count[num[end]]++;
        if(count[num[end]] == (K + 1)){
            while(num[start] != num[end]) {count[num[start]]--; start++;}
            count[num[end]]--; start++;
        }
        max_length = max(end-start + 1, max_length);
        end++;
    }
    cout << max_length;
}