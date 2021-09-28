// 121. Best Time to Buy and Sell Stock (Easy)
// Runtime: 96 ms, faster than 98.13% of C++ online submissions for Best Time to Buy and Sell Stock.
// Memory Usage: 93.4 MB, less than 53.95% of C++ online submissions for Best Time to Buy and Sell Stock.

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int N = prices.size();
        int answer = 0;
        int min_val = prices[0];
        for(int i = 0; i < N; i++){
            answer = max(answer, prices[i]-min_val);
            min_val = min(min_val, prices[i]);
        }
        return answer;
    }
};

// N^2 time limit