#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
//https://jaimemin.tistory.com/682 참고 ㅠ
//nCr=(n-1)C(r-1)+(n-1)Cr
string result[101][101];
string BigIntAdd(string a,string b){
    long long sum = 0;
    string res;
    while(!a.empty()||!b.empty()||sum){
        if(!a.empty()){
            sum += a.back() - '0';
            a.pop_back();
        }
        if(!b.empty()){
            sum += b.back() - '0';
            b.pop_back();
        }
        res.push_back((sum%10) + '0');
        sum /= 10;
    }
    reverse(res.begin(), res.end());
    return res;
}

string combination(int n, int m){
    if(n == m || m == 0) return "1";
    string res = result[n][m];
    if(res != "")
        return res;
    res = BigIntAdd(combination(n-1,m-1), combination(n-1, m));
    result[n][m] = res;
    return res;
}
int main(){
    int n,m; cin >> n >> m;
    if(m > (n/2) && m != n) m = n-m;
    cout << combination(n,m);
}
