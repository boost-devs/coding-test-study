###### 2224번: 명제 증명
# https://www.acmicpc.net/problem/2224
# 메모리/시간: KB / ms

import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N = int(input())

_input = set(input().rstrip() for _ in range(N))

proposition = defaultdict(list)

for x in _input:
    P, Q = x.split(" => ")
    proposition[P].append(Q)

def bfs(x):
    _return = []
    cnt = 0
    queue = deque([x])
    while queue:
        z = queue.popleft()
        if z in proposition.keys():
            for v in proposition[z]:
                if v not in _return and v != x:
                    _return.append(v)
                    queue.append(v)
                    cnt += 1
    return _return, cnt

answer = defaultdict(list)
cnt = 0

for k in proposition.keys():
    _return, leng = bfs(k)
    answer[k] = sorted(_return)
    cnt += leng

print(cnt)
for k in sorted(proposition.keys()):
    for x in answer[k]:
        print(f"{k} => {x}")