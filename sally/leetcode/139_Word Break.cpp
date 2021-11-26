// 139. Word Break
// Runtime: 40 ms, faster than 15.17 % of C++ online submissions for Word Break.
// Memory Usage : 13.1 MB, less than 51.69 % of C++ online submissions for Word Break.
// ref: https://leetcode.com/problems/word-break/discuss/43814/C%2B%2B-Dynamic-Programming-simple-and-fast-solution-(4ms)-with-optimization

class Solution {
public:
    bool dp[302] = { false, };
    bool wordBreak(string s, vector<string>& words) {
        int s_len = s.size();
        dp[0] = true;
        for (int i = 1; i <= s_len; i++) {
            for (int j = 0; j < i; j++) {
                if (dp[j]) {
                    string target = s.substr(j, i - j);
                    for (auto k : words)
                        if (k == target) {
                            dp[i] = true;
                        }
                }
            }
        }
        for (auto i : dp) cout << i << ' ';
        cout << '\n';
        return dp[s_len];
    }
};