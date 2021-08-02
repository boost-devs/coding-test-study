#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <vector>
using namespace std;

bool cmp(long long int a, long long int b){
    if(abs(a) <= abs(b)) return true;
    return false;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N; cin >> N;
    long long int arr[10000001];
    for(int i = 0;i<N;i++) cin >> arr[i];
    sort(arr, arr + N, cmp);
    int a, b; long long int Min = 3e9;
    for(int i = 1;i<N;i++){
        if(Min > abs(arr[i-1] + arr[i])){
            a = i-1; b = i;
            Min = abs(arr[i-1] + arr[i]);
        }
    }
    cout << (arr[a] < arr[b]? arr[a] : arr[b]) << " " << (arr[a] < arr[b]? arr[b] : arr[a]);
}