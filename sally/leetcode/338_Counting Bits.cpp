// 338. Counting Bits
// Runtime: 8 ms, faster than 33.39% of C++ online submissions for Counting Bits.
// Memory Usage: 8.4 MB, less than 38.35% of C++ online submissions for Counting Bits.

class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> result;
        result.push_back(0);
        for(int i = 1; i <= n; i++){
            int target = i;
            int res = 1;
            while(1){
                if(target == 1) break;
                if(target % 2 == 1) res++;
                target /= 2;
            }
            result.push_back(res);
        }
        return result;
    }
};