# 문제: 139. Word Break
# 링크: https://leetcode.com/problems/word-break/

# 시간/공간: 32ms / 14.3MB
# 참고: https://leetcode.com/problems/word-break/discuss/43808/Simple-DP-solution-in-Python-with-description
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        table = [False] * (len(s) + 1)
        table[0] = True
        for i in range(1, len(s) + 1):
            for word in wordDict:
                if table[i - len(word)] and s[i - len(word) : i] == word:
                    table[i] = True
        return table[-1]
