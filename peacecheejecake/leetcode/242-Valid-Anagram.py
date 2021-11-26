from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def count(x):
            return set(Counter(x).items())
        return count(s) == count(t)
        