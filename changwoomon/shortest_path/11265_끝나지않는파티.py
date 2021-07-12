###### 11265번: 끝나지 않는 파티
# https://www.acmicpc.net/problem/11265
# 메모리/시간: 127152KB / 500ms (PyPy3)

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]


for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for _ in range(M):
    A, B, C = map(int, input().split())
    A, B = A - 1, B - 1
    
    print("Enjoy other party") if graph[A][B] <= C else print("Stay here")