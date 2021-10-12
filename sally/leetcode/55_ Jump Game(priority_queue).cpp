// 55. Jump Game

// sol1
// Runtime: 618 ms, faster than 9.28% of C++ online submissions for Jump Game.
// Memory Usage: 52.3 MB, less than 5.03% of C++ online submissions for Jump Game.

// sol2
// Runtime: 438 ms, faster than 13.17% of C++ online submissions for Jump Game.
// Memory Usage: 52.3 MB, less than 5.03% of C++ online submissions for Jump Game.

// sol3
// Runtime: 305 ms, faster than 15.85% of C++ online submissions for Jump Game.
// Memory Usage: 52.4 MB, less than 5.03% of C++ online submissions for Jump Game.

// sol3
static bool _foo = ios::sync_with_stdio(false);
static ostream *_bar = cin.tie(NULL);

#include <queue>

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int cur = 0;
        bool visit[100001] = {false,};
        int n_len = nums.size();
        priority_queue<int> q;
        
        if(n_len == 0 || n_len == 1) return true;
        
        visit[cur] = true;
        q.push(cur);
        
        while(!q.empty()){
            cur = q.top();
            q.pop();
            
            if(cur == n_len-1) return true;
            
            // sol2
            for(int i = nums[cur]; i >= 1; i--){ // 438ms
                int target = cur+i;
                if(target >= n_len) continue;
                if(!visit[target]) {
                    q.push(target);
                    visit[target] = true;
                }
            }    

            // sol1
            // for(int i = 1; i <= nums[cur]; i++){ // 618ms
            //     int target = cur+i;
            //     if(target >= n_len) break;
            //     if(!visit[target]) {
            //         q.push(target);
            //         visit[target] = true;
            //     }
            // }       
        }
        return false;
    }
};