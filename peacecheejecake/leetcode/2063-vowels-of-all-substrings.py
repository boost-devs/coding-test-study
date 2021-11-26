class Solution:
    def countVowels(self, word: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        answer = 0
        for i, char in enumerate(word):
            if char in vowels:
                answer += (i + 1) * (len(word) - i)
        return answer


# Runtime: 136 ms
# Memory Usage: 15 MB
