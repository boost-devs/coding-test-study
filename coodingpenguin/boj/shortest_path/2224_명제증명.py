# 문제: [BOJ 2224] 명제 증명
# 유형: 플로이드
# 메모리/시간: 29452kb / 104ms

import sys

input = sys.stdin.readline
upper_base = ord('A')   # 대문자 시작 번호
lower_base = ord('a')   # 소문자 시작 번호

def char_to_ord(c):
    if c.isupper():
        return ord(c) - upper_base
    return ord(c) - lower_base + 26

def ord_to_char(n):
    if n < 26:
        return chr(upper_base + n)
    return chr(lower_base + n - 26)

n = int(input())
table = [[False]*52 for _ in range(52)] # 인접행렬
for _ in range(n):
    a, b = map(char_to_ord, input().rstrip().split(" => "))
    table[a][b] = True

for k in range(52):
    for i in range(52):
        for j in range(52):
            # 이어져 있다면 갱신
            if table[i][k] and table[k][j]:
                table[i][j] = True

result = []
for i in range(52):
    for j in range(52):
        # 시작과 도착이 같지 않고 길이 있다면
        if i != j and table[i][j]:
            prop = f"{ord_to_char(i)} => {ord_to_char(j)}"
            result.append(prop)

print(len(result))  # 명제 개수
for r in result:
    print(r)    # 가능한 명제