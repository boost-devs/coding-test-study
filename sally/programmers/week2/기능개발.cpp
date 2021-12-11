// https://programmers.co.kr/learn/courses/30/lessons/42586

#include <string>
#include <string.h>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speed) {
    vector<int> answer;
    int n = progresses.size();
    
    int cnt = 0;
    for(int i = 0; i < n; i++){
        if(progresses[i] >= 100) cnt++;
        else if(progresses[i]<100){
            if(cnt != 0) {
                answer.push_back(cnt);
                cnt = 0;
            }
            else {
                int need_days = 100 - progresses[i];
                if(need_days % speed[i] == 0) need_days = (need_days / speed[i]);
                else if(need_days % speed[i] != 0) need_days = (need_days / speed[i]) + 1;
                
                for(int j = i; j < n; j++){
                    progresses[j] += (need_days * speed[j]);
                }
            }
            i--;
        } 
    }
    if(cnt != 0) answer.push_back(cnt);
    
    return answer;
}