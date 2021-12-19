#include <iostream>
#include <vector>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N,M; cin >> N >> M;
    int A[1000005]; int B[1000005];
    fill_n(A, 1000005,1e9);fill_n(B, 1000005,1e9);
    for(int i = 0;i<N;i++) cin >> A[i];
    for(int i = 0;i<M;i++) cin >> B[i];
    int a = 0;int b = 0;
    while(a != N || b != M){
        if((A[a] <= B[b]) || b == M){
            cout << A[a] << " ";
            a++;
        }
        else if((B[b] < A[a]) || a == N){
            cout << B[b] << " ";
            b++;
        }
    }
}