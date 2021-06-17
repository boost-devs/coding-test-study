# 문제: [BOJ 14675] 단절점과 단절선
# 유형: BFS
# 메모리/시간: 29904kb / 272ms

import sys

input = sys.stdin.readline

N = int(input())  # 정점 개수
degrees = [0] * (N + 1)  # 각 정점 별 간선 개수

for _ in range(N - 1):
    a, b = map(int, input().split())
    degrees[a] += 1
    degrees[b] += 1


Q = int(input())  # 질문 개수
for _ in range(Q):
    t, k = map(int, input().split())  # 질문 유형, 정점/간선 번호
    # 단절점 질문
    if t == 1:
        if degrees[k] == 1:
            print("no")
        else:
            print("yes")
    # 단절선 질문
    else:
        print("yes")
