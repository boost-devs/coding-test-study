###### 2668번: 숫자고르기
# https://www.acmicpc.net/problem/2668
# 메모리/시간: 29200KB / 76ms

import sys

input = sys.stdin.readline

N = int(input())

row = [0 for _ in range(N+1)]

for i in range(1, N+1):
    row[i] = int(input())

def dfs(v, i):
    visited[v] = True
    x = row[v]
    if not visited[x]:
        dfs(x, i)
    elif visited[x] and (x == i):
        result.append(x)

result = []

for i in range(1, N+1):
    visited = [False for _ in range(N+1)]
    dfs(i, i)

print(len(result))
print("\n".join(map(str, result)))