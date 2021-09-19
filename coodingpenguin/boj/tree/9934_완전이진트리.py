# 문제: [BOJ 9934] 완전 이진 트리
# 유형: 트리
# 메모리/시간: 32048kb / 88ms

import sys
from collections import defaultdict

input = sys.stdin.readline

# 입력
K = int(input())  # 트리 레벨
paths = list(map(int, input().split()))  # 방문 순서

levels = [K]  # 방문 순서별 트리 레벨
for i in range(K - 1, 0, -1):
    levels = levels + [i] + levels

tree = defaultdict(list)  # 레벨 별 노드
for pos, level in enumerate(levels):
    tree[level].append(paths[pos])

# 출력
for _, nodes in sorted(tree.items()):
    print(*nodes)
