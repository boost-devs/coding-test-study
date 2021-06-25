# 문제: [BOJ 10870] 피보나치 수5
# 유형: 동적계획법
# 메모리/시간: 29200kb / 72ms

import sys

input = sys.stdin.readline
inf = int(1e9)

n = int(input())  # 킬로그램
l = n + 1 if n >= 5 else 6  # 테이블 길이

# 테이블 생성 및 초기화
table = [inf] * l
table[3] = 1
table[5] = 1

# 테이블 채우기
for i in range(6, n + 1):
    table[i] = min(table[i - 3] + 1, table[i - 5] + 1)

# 만들 수 없다면
if table[n] >= inf:
    print(-1)
# 만들 수 있다면
else:
    print(table[n])
