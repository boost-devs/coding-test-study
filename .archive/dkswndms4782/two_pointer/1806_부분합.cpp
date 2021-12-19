#include <iostream>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N,S; cin >> N >> S;
    int num[100001];
    for(int i = 0;i<N;i++) cin >> num[i];
    int start = 0; int end = 0; int result = 100001; int sum = 0;
    while(end != (N + 1)){
        if(sum >= S){
            while(sum >= S && start != end){
                result = min(result, end-start);
                sum -= num[start];
                start++;
            }
        }
        else{
            if(end == (N+1)) continue;
            sum += num[end];
            end++;
        }
    }

    if(result == 100001) cout << 0;
    else cout << result;
}