#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int N,M,R; cin >> N  >> M  >> R;
    int arr[301][301];
    for(int i = 0;i<N;i++) for(int j = 0;j<M;j++) cin >> arr[i][j];
    int cnt = min(N,M)/2;
    for(int i  = 0;i<R;i++){
        for(int j = 0;j<cnt;j++){
            int tmp = arr[j][j]; //복사하고 남은 마지막 저장
            for(int k = j+1;k<M-j;k++) arr[j][k-1] = arr[j][k];
            for(int k = j+1;k<N-j;k++) arr[k-1][M-1-j] = arr[k][M-1-j];
            for(int k = M-2-j;k>=j;k--) arr[N-1-j][k+1] = arr[N-1-j][k];
            for(int k = N-2-j;k>=j;k--) arr[k+1][j] = arr[k][j];
            arr[j+1][j] = tmp;
        }
    }
    for(int i = 0;i<N;i++) {
        for(int j = 0;j<M;j++){
            cout << arr[i][j] << " ";
        }
        cout << "\n";
    }
}