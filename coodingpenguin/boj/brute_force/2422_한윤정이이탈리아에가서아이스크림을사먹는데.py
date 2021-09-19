# 문제: [BOJ 2422] 한윤정이 이탈리아에 가서 아이스크림을 사먹는데
# 유형: 완전 탐색
# 메모리/시간: 32748kb / 1040ms

import sys
from collections import defaultdict

input = sys.stdin.readline


# 입력
n, m = map(int, input().split())  # 아이스크림 수, 조합 수
unmatch = defaultdict(list)  # 있으면 안 될 조합들
for _ in range(m):
    a, b = map(int, input().split())
    unmatch[a].append(b)
    unmatch[b].append(a)

count = 0  # 가능한 조합 개수
for i in range(1, n + 1):
    for j in range(i, n + 1):
        # 안 되는 조합이거나 같은 아이스크림이면
        if j in unmatch[i] or i == j:
            continue
        for k in range(j, n + 1):
            # 안 되는 조합이거나 같은 아이스크림이면
            if k in unmatch[i] or k in unmatch[j] or i == k or j == k:
                continue
            count += 1  # 가능한 경우만 카운트

print(count)
