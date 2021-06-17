###### 14675번: 단절점과 단절선
# https://www.acmicpc.net/problem/14675
# 메모리/시간: 44316KB / 320ms

import sys

input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

q = int(input())
for _ in range(q):
    t, k = map(int, input().split())
    cond = False
    
    if t == 1:
        if len(tree[k]) > 1:
            cond = True
    else:
        cond = True

    if cond:
        print("yes")
    else:
        print("no")