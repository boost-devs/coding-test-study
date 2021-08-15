#include <iostream>
using namespace std;

int arr[25][25];
int direction[4][2] = {{0,1},{1,1},{1,0},{1,-1}};

int dfs(int a, int b ,int di,int count){
    int tmp_a = a + direction[di][0];
    int tmp_b = b + direction[di][1];
    if(tmp_a > 0 && tmp_b > 0 && tmp_a < 20 && tmp_b < 20 && arr[tmp_a][tmp_b] == arr[a][b]){
        return dfs(tmp_a, tmp_b, di,count + 1);
    }
    return count;
}

int main(){
    for(int i = 1;i<20;i++) for(int j = 1;j<20;j++) cin >> arr[i][j];
    for(int i = 1;i<20;i++){
        for(int j = 1;j<20;j++){
            if(arr[i][j] != 0){
                for(int k = 0;k<3;k++){
                    if(arr[i - direction[k][0]][j - direction[k][1]] == arr[i][j]) continue;
                    if(dfs(i,j,k,1) == 5){
                        cout << arr[i][j] << "\n";
                        cout << i << " " << j;
                        return 0;
                    }
                }
                if(dfs(i,j,3,1) == 5 && arr[i - direction[3][0]][j - direction[3][1]] != arr[i][j]){
                        cout << arr[i][j] << "\n";
                        cout << (i+4) << " " << (j-4);
                        return 0;
                }
            }
        }
    }
    cout << 0;
}