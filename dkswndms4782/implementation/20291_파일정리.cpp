#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;

vector<string> split(string input, char delimiter) {
    vector<string> answer;
    stringstream ss(input);
    string temp;
    while (getline(ss, temp, delimiter)) {
        answer.push_back(temp);
    }
    return answer;
}

int main(){
    int N; cin >> N;
    string t;
    vector<string>v;
    map<string,int>m;
    while(N--){
        cin >> t;
        vector<string> tmp = split(t,'.');
        m[tmp[1]] += 1;
        if( m[tmp[1]] == 1) v.push_back(tmp[1]);
    }
    // v.erase(unique(v.begin(),v.end()),v.end());
    sort(v.begin(), v.end());
    for(int i = 0;i<v.size();i++){
        cout << v[i] << " ";
        cout << m.find(v[i]) -> second << "\n";
    }
}