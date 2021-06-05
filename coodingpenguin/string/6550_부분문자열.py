# 문제: [BOJ 6550] 부분 문자열
# 유형: 문자열, 스택
# 메모리/시간: 29200kb / 76ms

import sys


def check(s, t):
    # 붙어있는 형태로 부분 문자열인 경우
    if s in t:
        return True
    # 떨어져 있는 형태로 부분 문자열인 경우
    stack = list(s)
    for letter in t:
        if not stack:
            return True
        if stack[0] == letter:
            stack.pop(0)
    # 부분 문자열이 아닌 경우
    return False


for line in sys.stdin:
    # 입력
    s, t = line.rstrip().split()
    # s가 t의 부분 문자열이라면
    if check(s, t):
        print("Yes")
    # 아니라면
    else:
        print("No")
