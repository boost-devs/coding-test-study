#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
#include <deque>
using namespace std;

int N; deque<int>result;

bool check(deque<int>a, deque<int>b){
    int Size = a.size();
    while(Size--){
        if(a.front() != b.front()) return false;
        a.pop_front(); b.pop_front();
    }
    return true;
}

deque<int> func(deque<int>s, int k){
    deque<int>result;
    while(k >= 0){
        deque<int>s_front,s_back;
        int s_size = s.size();
        for(int i = 0;i<(s_size-pow(2,k));i++){
            s_front.push_back(s.front()); s.pop_front();
        }
        for(int i = (s_size-pow(2,k));i<s_size;i++){
            s_back.push_back(s.front()); s.pop_front();
        }
        s = s_back;
        while(!s_front.empty()){result.push_front(s_front.back()); s_front.pop_back();}
        k--;
    }
    result.push_front(s.front());
    return result;
}

int main(){
    cin >> N; int t; deque<int>card;
    for(int i = 1;i<=N;i++) {card.push_back(i); cin >> t; result.push_back(t);}
    int K_max = int(log2(N));
    if(pow(2,K_max) == N) K_max--;
    deque<int> card_1[1001]; //k : index
    for(int k = 1;k<=K_max;k++){
        card_1[k] = func(card,k);
    }
    for(int k1 = 1;k1<=K_max;k1++){
        for(int k2 = 1;k2 <= K_max;k2++){
            if(check(result, func(card_1[k1], k2))) {cout << k1 << " " << k2; return 0;}
        }
    }

}