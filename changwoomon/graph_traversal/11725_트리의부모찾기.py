# 11725번: 트리의 부모 찾기
# https://www.acmicpc.net/problem/11725
# 메모리/시간: 132484KB / 404ms

import sys

# 런타임 에러
sys.setrecursionlimit(10**6) # RecursionError 해결
input = sys.stdin.readline

# DFS 메서드 정의
def dfs(start, parent):
    for i in tree[start]:
        if parent[i]==0:
            parent[i] = start
            dfs(i, parent)

N = int(input())

tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    start, end = map(int, input().split())
    tree[start].append(end)
    tree[end].append(start)

parent = [0 for _ in range(N+1)]

dfs(1, parent)

for i in range(2, N+1):
    print(parent[i])