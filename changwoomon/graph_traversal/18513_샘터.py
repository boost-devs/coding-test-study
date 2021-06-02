###### 18513번: 샘터
# https://www.acmicpc.net/problem/18513
# 메모리/시간: 50788KB / 300ms

import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

_sam = list(map(int, input().split()))

dx = [-1, 1]

def bfs(_sam):
    global K
    queue = deque(_sam)
    visited = set()
    for x in _sam:
        visited.add(x)
    unhappiness = 0
    answer = 0
    while queue:
        unhappiness += 1
        if unhappiness > 100000000:
            return None
        for _ in range(len(queue)):
            x = queue.popleft()
            for way in range(2):
                if K == 0:
                    return answer
                xx = x + dx[way]
                if (xx <= -200000000) or (xx >= 200000000) or (xx in visited):
                    continue
                if xx not in visited:
                    K -= 1
                    answer += unhappiness
                    queue.append(xx)
                    visited.add(xx)

print(bfs(_sam))