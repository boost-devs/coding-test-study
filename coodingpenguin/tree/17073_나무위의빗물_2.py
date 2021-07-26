# 문제: [BOJ 17073] 나무 위의 빗물
# 유형: 트리
# 메모리/시간: 157464kb / 1704ms

import sys
from collections import defaultdict

input = sys.stdin.readline

N, W = map(int, input().split())  # 노드 수, 물의 양
tree = defaultdict(list)  # 트리
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

leaves = []  # 리프 노드
for i in range(2, N + 1):
    if len(tree[i]) == 1:
        leaves.append(i)

# 출력
print(W / len(leaves))
