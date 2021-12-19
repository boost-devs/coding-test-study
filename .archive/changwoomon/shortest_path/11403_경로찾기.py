###### 11403번: 경로 찾기
# https://www.acmicpc.net/problem/11403
# 메모리/시간: 29452KB / 148ms

import sys

input = sys.stdin.readline

N = int(input())

_map = [list(map(int, input().split())) for _ in range(N)]

def dfs(x):
    for i in range(N):
        if (_map[x][i] == 1) and (visited[i] == 0):
            visited[i] = 1
            dfs(i)

for i in range(N):
    visited = [0] * N
    dfs(i)
    print(*visited)