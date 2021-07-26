#include <iostream>
#include <string>
using namespace std;

string mul(string a, int b){
    string result = "";
    for(int i = 0;i<b;i++){
        result += a;
    }
    return result;
}

string make_arr(int idx , int N){
    string result = "";
    int count = idx/2;
    string left = mul("* ", count);
    string right = mul(" *", count);
    if(idx%2 == 0){
        string mid = mul("*", N-4*count);
        result += (left + mid + right);
    }
    else{
        string mid = '*' + mul(" ", N-2-4*count) + "*";
        result += (left + mid + right);
    }
    return result;
}

int main(){
    int N;cin >> N;
    string result[401];
    int idx = (1 + (N-1)*4);
    int count = 0;
    for(int i = 0;i<(idx/2);i++){
        result[i] = make_arr(i, idx);
        result[idx-i-1] = result[i];
    }
    result[idx/2] = mul("* ", idx/2 + 1);
    for(int i = 0;i<idx;i++)
        cout << result[i] << "\n";
}