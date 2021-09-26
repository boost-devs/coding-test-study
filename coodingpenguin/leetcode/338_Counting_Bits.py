# 문제: 338. Counting Bits
# 링크: https://leetcode.com/problems/counting-bits/

# 시간/공간: O(NM) / O(N)
# N: 숫자, M: 이진수 변환 시 길이
class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = []
        for i in range(n + 1):
            answer.append(bin(i).count("1"))
        return answer
