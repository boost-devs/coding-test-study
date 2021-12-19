#include <iostream>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N,X; cin >> N >> X;
    int arr[250001];
    for(int i = 0;i<N;i++) cin >> arr[i];
    int start = 0; int end =  X; int sum = 0;
    for(int i = 0;i<X;i++) sum += arr[i]; int Max = sum; int count = 1;
    while(end != N){
        sum -= arr[start];
        sum += arr[end];
        if(Max < sum){
            Max = sum; count = 1;
        }
        else if(Max == sum) count++;
        start++; end++;
    }
    if(sum == 0)cout << "SAD";
    else cout << Max << "\n" << count;
}