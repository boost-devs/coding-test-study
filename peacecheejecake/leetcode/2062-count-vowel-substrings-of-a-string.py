vowels = {'a', 'e', 'i', 'o', 'u'}


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        if len(word) < 5 or vowels - set(word):
            return 0
        
        conso_indices = []
        for i, char in enumerate(word):
            if char not in vowels:
                conso_indices.append(i)

        answer = 0
        if not conso_indices:
            for start in range(len(word) - 4):
                for end in range(start + 5, len(word) + 1):
                    subphrase = set(word[start:end])
                    if subphrase == vowels:
                        answer += 1
        else:
            last_conso_idx = 0
            for conso_idx in conso_indices:
                answer += self.countVowelSubstrings(word[last_conso_idx + 1:conso_idx])
                last_conso_idx = conso_idx
            answer += self.countVowelSubstrings(word[conso_idx + 1:])
        return answer

# Runtime: 132 ms
# Memory Usage: 14.3MB
