###### 13549번: 숨바꼭질 3
# https://www.acmicpc.net/problem/13549
# 메모리/시간: 131664KB / 6368ms (PyPy3)

import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

f1 = lambda x: x-1
f2 = lambda x: x+1
f3 = lambda x: 2*x
func = [f3, f1, f2]

def check(x, cnt):
    for i, f in enumerate(func):
        xx = f(x)
        find = []
        if (xx < 0) or (xx > 100000):
            continue
        if xx not in visited:
            visited.append(xx)
            if xx == K:
                find.append(True)
                if i == 0:
                    return any(find), cnt
                else:
                    return any(find), cnt + 1
            else:
                find.append(False)
                if i == 0:
                    queue.append([xx, cnt])
                else:
                    queue.append([xx, cnt+1])
    return any(find), cnt

def bfs(X):
    while queue:
        for _ in range(len(queue)):
            x, cnt = queue.popleft()
            if x == K:
                return cnt
            cond, tmp = check(x, cnt)
            if cond:
                return tmp

cnt = 0
queue = deque([[N, cnt]])
visited = [N]
print(bfs(N))