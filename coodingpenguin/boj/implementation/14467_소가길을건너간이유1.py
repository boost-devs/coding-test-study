# 문제: [BOJ 14467] 소가 길을 건나간 이유1
# 유형: 구현
# 메모리/시간: 31824kb / 88ms

import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())  # 관찰 횟수
count = 0  # 길을 건너간 최소 횟수
loc = defaultdict(int)  # 소의 최근 위치
for _ in range(n):
    a, b = map(int, input().split())  # 번호, 위치
    # 최근 위치 정보가 없다면
    if a not in loc:
        loc[a] = b
    # 최근 위치 정보가 있다면
    else:
        if loc[a] != b:
            loc[a] = b  # 갱신
            count += 1
print(count)
