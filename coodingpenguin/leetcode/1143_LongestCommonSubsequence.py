# 문제: 1143. Longest Common Subsequence
# 링크: https://leetcode.com/problems/longest-common-subsequence/


# 시간/공간: 392ms / 21.9MB
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        table = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]  # DP 테이블
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                # i와 j가 가리키는 각 문자가 같다면
                if text1[i - 1] == text2[j - 1]:
                    # 두 문자 전의 테이블값에 +1
                    table[i][j] = table[i - 1][j - 1] + 1
                else:
                    # 두 문자의 각 전의 테이블 값 중 큰 값을 가져온다
                    table[i][j] = max(table[i - 1][j], table[i][j - 1])
        return table[len(text1)][len(text2)]
