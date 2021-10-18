# 문제: 190. Reverse Bits
# 링크: https://leetcode.com/problems/reverse-bits/


# 시간/공간: 32ms / 14.3MB
class Solution:
    def reverseBits(self, n: int) -> int:
        return int("{:032b}".format(n)[::-1], 2)
