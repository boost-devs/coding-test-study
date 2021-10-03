# 문제: [BOJ 16171] 나는 친구가 적다(Small)
# 유형: 문자열
# 메모리/시간: 29200kb / 72ms

import sys

input = sys.stdin.readline


def clean_str(s):
    result = ""
    for letter in s:
        # 숫자가 아닌 것만 추가
        if not letter.isdigit():
            result += letter
    return result


# 입력
s = clean_str(input().rstrip())
k = input().rstrip()

# 출력
print(int(k in s))
