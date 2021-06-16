/*
# Tree
# Problem: 6418
# Memory: 2024KB
# Time: 0ms
*/
#include <iostream>
#include <string.h>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <algorithm>
#include <cmath>
#include <deque>
#include <map>
#include <set>
using namespace std;

set<int> s, s_in, s_all;
char c, a_, b_;
int a = -2, b = -2;
int N = 0;
int v_cnt = 0;

void init(){
    a = -2; b = -2;
    s.clear();
    s_in.clear();
    s_all.clear();
    v_cnt = 0;
}

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    set<int>::iterator iter;
    while(1){
        N++;
        init();
        bool empty_tree = true;
        bool failed = false;
        cin >> a;
        cin >> b;
        s_in.insert(a);
        s.insert(b);
        s_all.insert(a);
        s_all.insert(b);
        v_cnt++;

        while(1){
            if(a == 0 && b == 0) break;
            if(a == -1 && b == -1) break;
            if (a == b) {
                empty_tree = false;
                failed = true;
            }
            cin >> a;
            cin >> b;
            s_all.insert(a);
            s_all.insert(b);
            v_cnt++;

            if(a != 0 || b != 0) empty_tree = false;

            iter = s.find(b);
            if(iter != s.end()) failed = true;
            else s.insert(b);
            s_in.insert(a);
        }
        if(a == -1 && b == -1) break;
        else if (empty_tree) { // 빈 노드
            cout << "Case " << N << " is a tree.\n";
            continue;
        }

        for(auto i : s){
            iter = s_in.find(i);
            if(iter != s_in.end()){
                s_in.erase(i);
            }
        }
        if(s_in.size() == 0) failed = true;
        if(v_cnt+1 != s_all.size()) failed = true; // cause of 50% acc

        if(failed){
            cout << "Case " << N << " is not a tree.\n";
        } else cout << "Case " << N << " is a tree.\n";
    }

    return 0;
}
