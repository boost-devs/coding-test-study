#include <iostream>
#include <string>
using namespace std;

int Max = -1;
int Min = 1000000000;

int count_odd(int num){
    int cnt = 0;
    while(num != 0){
        if(num % 2 == 1) cnt++;
        num/=10;
    }
    return cnt;
}

void my_func(string tmp, int count){
    if(tmp.length() >= 3){
        for(int i = 1;i<=tmp.length();i++){
            for(int j = 1;(i + j)<tmp.length();j++){
                int s1 = stoi(tmp.substr(0, i));
                int s2 = stoi(tmp.substr(i, j));
                int s3 = stoi(tmp.substr(i + j, tmp.length()));
                string t = to_string(s1 + s2 + s3);
                my_func(t, count + count_odd(stoi(tmp)));
            }
        }
    }
    else if(tmp.length() == 2){
        int t1 = stoi(tmp) / 10;
        int t2 = stoi(tmp) % 10;
        string t = to_string(t1 + t2);
        my_func(t, count + count_odd(stoi(tmp)));

    }
    else if(tmp.length() == 1){
        int t = stoi(tmp);
        count += (t%2);
        Min = (Min > count ?count : Min);
        Max = (Max < count?count : Max);
    }
}

int main(){
    int N;cin >> N;
    string Num = to_string(N);
    my_func(Num, 0);
    cout << Min << " " << Max;
}