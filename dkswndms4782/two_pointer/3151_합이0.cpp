#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N; cin >> N; int arr[100001];
    for(int i = 0;i<N;i++) cin >> arr[i];
    sort(arr, arr + N);
    long long int count = 0;
    for(int i = 0; i<(N-2);i++){
        for(int j = i+1; j<(N-1);j++){
            int tmp = (-1) * (arr[i] + arr[j]);
            int i1 = lower_bound(arr+j+1, arr+N, tmp) - arr;
            int i2 = upper_bound(arr+j+1, arr+N, tmp) - arr;
            count += (i2 - i1);
        }
    }
    cout << count;
}