# 문제: [BOJ 17073] 나무 위의 빗물
# 유형: 트리
# 메모리/시간: 162116kb / 2436ms

import sys
from collections import defaultdict, deque

input = sys.stdin.readline


def bfs(root):
    queue = deque([root])
    while queue:
        v = queue.popleft()
        # 자식 노드의 개수
        num_of_child = len(tree[v]) - 1 if v != 1 else len(tree[v])
        for i in tree[v]:
            if not water[i]:
                water[i] = water[v] / num_of_child
                queue.append(i)


N, W = map(int, input().split())  # 노드 수, 물의 양
tree = defaultdict(list)  # 트리
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# 리프 노드
leaves = []
for i in range(2, N + 1):
    if len(tree[i]) == 1:
        leaves.append(i)

water = [0] * (N + 1)  # 각 노드별 물의 양 기댓값
water[1] = W  # 루트 노드는 W로 초기화

# 너비 우선 탐색
bfs(1)

# 출력
result = sum([water[i] for i in leaves]) / len(leaves)
print(result)
