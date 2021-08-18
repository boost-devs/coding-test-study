#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
using namespace std;

int N; string card = "";

string func(string s, int k){
    string result = "";
    while(k >= 0){
        string s_front = "";string s_back = "";
        for(int i = 0;i<(s.size()-pow(2,k));i++){
            s_front += s[i];
        }
        for(int i = (s.size()-pow(2,k));i<s.size();i++){
            s_back += s[i];
        }
        s = s_back;
        result = s_front + result;
        k--;
    }
    result = s + result;
    return result;
}

int main(){
    cin >> N; int t; string result = "";
    for(int i = 1;i<=N;i++) {card += to_string(i); cin >> t; result += to_string(t);}
    int K_max = int(log2(N));
    string card_1[1001]; //k : index
    for(int k = 1;k<=K_max;k++){
        card_1[k] = func(card,k);
    }
    for(int k1 = 1;k1<=K_max;k1++){
        for(int k2 = 1;k2 <= K_max;k2++){
            if(result == func(card_1[k1], k2)) {cout << k1 << " " << k2; return 0;}
        }
    }

}