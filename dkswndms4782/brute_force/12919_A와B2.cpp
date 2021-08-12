#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

string S,T;
string AFunc(string S){
    S.pop_back();
    return S;
}
string BFunc(string S){
    reverse(S.begin(), S.end());
    S.pop_back();
    return S;
}
bool func(string S,string T){
    if(S.size() == T.size()){
        if(S == T) return true;
        return false;
    }
    if(T.size() >= 1){
        if(T.front() == 'A' && T.back() == 'A') return func(S, AFunc(T));
        if(T.front() == 'B' && T.back() == 'A') return func(S, AFunc(T)) || func(S, BFunc(T));
        if(T.front() == 'B' && T.back() == 'B') return func(S, BFunc(T));
        return false;
    }
}

int main(){
    cin >> S >> T;
    if(func(S,T)) cout << 1;
    else cout << 0;
}