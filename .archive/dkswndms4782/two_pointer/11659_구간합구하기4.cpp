#include <iostream>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int s[100001];
    int N,M; cin >> N >> M;
    int arr[100001]; int a,b;
    for(int i = 1;i<=N;i++) cin >> arr[i];
    for(int i = 1;i<=N;i++) s[i] = (s[i-1] + arr[i]);
    for(int i = 0;i<M;i++){
        cin >> a >> b;
        cout << s[b] - s[a - 1] << "\n";
    }
}