#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <math.h>
#include <algorithm>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    int remain[10] = { 0, };
    pair<int, bool> target;
    queue<pair<int, bool>> q;

    for (int i = 0; i < priorities.size(); i++) {
        remain[priorities[i]]++;

        if (i == location) q.push({ priorities[i], true });
        else q.push({ priorities[i], false });
    }

    while (1) {
        target = q.front();
        q.pop();

        bool pushed = false;
        for (int i = 9; i > target.first; i--) { // 더 큰 우선순위가 있는지 확인
            if (remain[i] > 0) {
                q.push(target);
                pushed = true;
                break;
            }
        }
        if (pushed == false) {
            answer++;
            remain[target.first]--;
            if (target.second == true) return answer;
        }
    }

    return answer;
}