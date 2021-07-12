# 문제: [BOJ 11265] 끝나지 않는 파티
# 유형:
# 메모리/시간: 	32012kb / 7808ms

import sys

input = sys.stdin.readline

n, m = map(int, input().split())  # 파티장 크기, 손님 수
graph = []  # 인접 행렬
for _ in range(n):
    graph.append(list(map(int, input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for _ in range(m):
    a, b, c = map(int, input().split())  # 시작, 도착, 시간
    # 제 시간에 도착할 수 있다면
    if graph[a - 1][b - 1] <= c:
        print("Enjoy other party")
    # 도착할 수 없다면
    else:
        print("Stay here")
