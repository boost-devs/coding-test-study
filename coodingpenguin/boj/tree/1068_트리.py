# 문제: [BOJ 1068] 트리
# 유형: 트리
# 메모리/시간: 32932kb / 96ms

import sys
from collections import defaultdict, deque

input = sys.stdin.readline


def bfs(start):
    count = 0  # 리프 노드 개수
    queue = deque([start])
    while queue:
        v = queue.popleft()
        # 자식이 없다면
        if v not in tree:
            count += 1
        # 자식이 있다면
        else:
            queue.extend(tree[v])  # 자식 큐에 추가
    return count


# 입력
N = int(input().rstrip())  # 노드 수
parents = list(map(int, input().split()))  # 부모테이블
removed = int(input().rstrip())  # 제거할 노드

tree = defaultdict(list)  # 트리
for i in range(N):
    # 자기나 부모가 제거할 노드라면
    if i == removed or parents[i] == removed:
        # 연결하지 않는다
        continue
    tree[parents[i]].append(i)

# 출력
if -1 not in tree:
    # 루트가 없다면
    print(0)
else:
    # 루트가 있다면
    root = tree[-1][0]
    # 너비 우선 탐색
    print(bfs(root))
