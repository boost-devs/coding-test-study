// 55. Jump Game
// Runtime: 817 ms, faster than 6.87% of C++ online submissions for Jump Game.
// Memory Usage: 51 MB, less than 5.03% of C++ online submissions for Jump Game.

#include <queue>

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int cur = 0;
        bool visit[100001] = {false,};
        int n_len = nums.size();
        queue<int> q;
        
        if(n_len == 0 || n_len == 1) return true;
        
        visit[cur] = true;
        q.push(cur);
        
        while(!q.empty()){
            cur = q.front();
            q.pop();
            
            if(cur == n_len-1) return true;
            
            for(int i = nums[cur]; i >= 1; i--){
                int target = cur+i;
                if(target >= n_len) continue;
                if(!visit[target]) {
                    q.push(target);
                    visit[target] = true;
                }
            }       
        }
        return false;
    }
};