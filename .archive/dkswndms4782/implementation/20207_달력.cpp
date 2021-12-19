#include <iostream>
using namespace std;

int main(){
    int N,S,E; cin >> N;
    int arr[400] = {0,};
    while(N--){
        cin >> S >> E;
        for(int i = S;i<=E;i++) arr[i]++;
    }
    int result = 0;
    int height = 0;
    int width = 0;
    for(int i = 1;i<= 366;i++){
        if(arr[i] == 0){
            result += (height * width);
            height = 0;
            width = 0;
        }
        else{
            height = (height < arr[i]?arr[i]:height);
            width++;
        }
    }
    cout << result;
}