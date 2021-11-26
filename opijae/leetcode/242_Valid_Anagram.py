from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        src_dict = defaultdict(int)  # src 단어에 있는 알파벳 개수 dict
        if len(s) != len(t): # 둘의 길이가 다르면 안됨
            return False
        for c in s: # 알파벳 dict 하나씩 채우기
            src_dict[c] += 1
        for c in t: # src 알파벳 dict에서 알파벳 하나씩 지우기
            if src_dict[c] == 0: # src에서 알파벳을 지울 수 없다면 안됨
                return False
            else:
                src_dict[c] -= 1
        return True