from collections import deque


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_lengths = {word: len(word) for word in wordDict}
        memo = set()
        stack = [0]
        while stack:
            start_idx = stack.pop()
            if start_idx in memo:
                continue
                
            memo.add(start_idx)
            for word, length in word_lengths.items():
                if word_lengths.get(s[start_idx:start_idx + length]) is not None:
                    if start_idx + length >= len(s):
                        return True
                    stack.append(start_idx + length)
        return False
        