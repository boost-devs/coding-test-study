# 문제: [BOJ 1316] 그룹 단어 체커
# 유형: 문자열
# 메모리/시간: 29200kb / 68ms

import sys

input = sys.stdin.readline


def check_group_word(word):
    for i in range(len(word)):
        letter = word[i]
        if i > 0:
            # 앞에 같은 문자가 있고 바로 앞 문자가 다를 문자일 경우
            if (letter in word[:i]) and (word[i - 1] != letter):
                # 그룹 단어가 아니므로 False 반환
                return False
    # 아무 문제 없으므로 True 반환
    return True


n = int(input())
count = 0
for _ in range(n):
    word = input().rstrip()
    if check_group_word(word):
        count += 1
print(count)
