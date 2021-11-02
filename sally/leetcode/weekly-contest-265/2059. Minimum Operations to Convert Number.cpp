class Solution {
public:
    int min_val = 1e9;
    int visit[1001] = {0,};
    vector<int> num;
    
    void dp(int cur, int goal, int dep){
        if (dep >= min_val) return;
        for(auto target : num){
            int target1 = cur - target;
            if(target1 == goal) {
                min_val = min(min_val, dep);
                return;
            }
            
            int target2 = cur + target;
            if(target2 == goal) {
                min_val = min(min_val, dep);
                return;
            }
            
            int target3 = cur ^ target;
            if(target3 == goal) {
                min_val = min(min_val, dep);
                return;
            }
            
            // valid range
            if(0 <= target1 && target1 <= 1000 && visit[target1] > dep+1){
                visit[target1] = dep+1;
                dp(target1, goal, dep+1);
            }
            if(0 <= target2 && target2 <= 1000 && visit[target2] > dep + 1){
                visit[target2] = dep+1;
                dp(target2, goal, dep+1);
            }
            if(0 <= target3 && target3 <= 1000 && visit[target3] > dep + 1){
                visit[target3] = dep+1;
                dp(target3, goal, dep+1);
            }
        }
    }
    
    int minimumOperations(vector<int>& nums, int start, int goal) {
        // init
        for(auto i :nums) num.push_back(i);
        for(int i = 0; i < 1001; i++) visit[i] = 1001;
        
        // dp
        visit[start] = 0;
        dp(start, goal, 1);
        if(min_val == 1e9) return -1;
        else return min_val;
        
    }
};