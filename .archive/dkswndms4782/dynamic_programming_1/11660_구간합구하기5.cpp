#include <iostream>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N,M; cin >> N >> M;
    int table[1025][1025] = {0,};
    for(int i = 1;i<= N;i++) {
        for(int j = 1;j<=N;j++) {
            cin >> table[i][j];
            table[i][j] += table[i][j-1];
        }
    }
    int x1,y1,x2,y2;
    while(M--){
        long long int result = 0;
        cin >> x1 >> y1 >> x2 >> y2;
        for(int i = x1; i<= x2;i++)
            result += (table[i][y2] - table[i][y1-1]);
        cout << result << "\n";
    }
}