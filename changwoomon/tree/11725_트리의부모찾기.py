# 11725번: 트리의 부모 찾기
# https://www.acmicpc.net/problem/11725
# 메모리/시간: 132912KB / 408ms

import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())

tree = [[] for _ in range(N+1)]
answer = [0 for _ in range(N+1)]

for _ in range(N-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

def dfs(s, parent):
    for i in tree[s]:
        if parent[i] == 0:
            parent[i] = s
            dfs(i, parent)

dfs(1, answer)

for i in range(2, N+1):
    print(answer[i])