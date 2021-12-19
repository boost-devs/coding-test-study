#include <iostream>
#include <vector>
using namespace std;

int main(){
    int H,W; cin >> H >> W;
    vector<int>v;
    int tmp; int result = 0;
    for(int i = 0;i<W;i++){
        cin >> tmp;
        v.push_back(tmp);
    }
    for(int i = 1;i<W-1;i++){
        int left = 0; int right = 0;
        for(int j = 0; j < i;j++) left = max(left, v[j]);
        for(int j = W-1;j > i;j--) right = max(right, v[j]);
        result += max(0, min(left, right) - v[i]);
    }
    cout << result;
 }