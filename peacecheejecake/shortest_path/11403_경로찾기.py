# https://www.acmicpc.net/problem/11403
# 경로 찾기
# 29200 KB / 636 ms


INF = int(1e9)
n = int(input())
graph = []
for _ in range(n):
    graph.append([
        1 if x == '1' else INF for x in input().split()
    ])

for v in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][v] < INF:
                min_dist = min(graph[i][j], graph[i][v] + graph[v][j])
                graph[i][j] = min_dist

for row in graph:
    print(' '.join('1' if x < INF else '0' for x in row))
