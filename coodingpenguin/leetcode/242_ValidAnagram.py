# 문제: 242. Valid Anagram
# 링크: https://leetcode.com/problems/valid-anagram/


# 시간/공간: 72ms / 14.5MB
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)
