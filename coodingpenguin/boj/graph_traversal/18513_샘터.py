# 문제: [BOJ 18513] 샘터
# 유형: BFS
# 메모리/시간: kb / ms

import sys
from collections import deque

input = sys.stdin.readline
direction = [1, -1]


def bfs(pos):
    queue = deque(pos)
    visited.append(pos)
    while queue:
        v = queue.popleft()


n, k = map(int, input().split())  # 샘터 개수, 집 개수
pos = list(map(int, input().split()))  # 샘터 위치
visited = []  # 방문한 위치

bfs(pos)
