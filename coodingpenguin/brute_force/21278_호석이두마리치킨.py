# 문제: [BOJ 21278] 호석이 두 마리 치킨
# 유형: 완전 탐색
# 메모리/시간: 29452kb / 524ms, 126396kb / 180ms (PyPy3)

import sys
from itertools import combinations

input = sys.stdin.readline
INF = int(1e9)


def floyd_warshall(n, m, graph):
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


def get_smallest_round_trip_time(n, graph):
    stores = None  # 최소 왕복시간 합 도시
    min_round_trip_time = INF  # 최소 왕복시간 합
    cases = list(combinations(range(1, n + 1), 2))  # 건물숫자 조합
    for a, b in cases:
        round_trip_time = sum(
            [min(i, j) * 2 for i, j in zip(graph[a][1:], graph[b][1:])]
        )
        # 기존 왕복시간 합보다 작다면
        if round_trip_time < min_round_trip_time:
            min_round_trip_time = round_trip_time  # 최소 왕복시간 합 갱신
            stores = (a, b)  # 최소 왕복시간 합 도시 갱신
    return stores[0], stores[1], min_round_trip_time


# 입력
n, m = map(int, input().split())  # 건물 수, 도로 수
graph = [[INF] * (n + 1) for _ in range(n + 1)]  # 도시 그래프

# 그래프 초기화
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1, n + 1):
    graph[i][i] = 0

floyd_warshall(n, m, graph)  # 최단 거리 계산

# 출력
print(*get_smallest_round_trip_time(n, graph))
