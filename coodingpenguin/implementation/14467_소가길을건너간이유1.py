# 문제: [BOJ 14467] 소가 길을 건나간 이유1
# 유형: 구현
# 메모리/시간: 31824kb / 88ms

import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
count = 0
loc = defaultdict(int)
for _ in range(n):
    a, b = map(int, input().split())
    if a not in loc:
        loc[a] = b
    else:
        if loc[a] != b:
            loc[a] = b
            count += 1
print(count)
