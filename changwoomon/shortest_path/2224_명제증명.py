###### 2224번: 명제 증명
# https://www.acmicpc.net/problem/2224
# 메모리/시간: 32084KB / 160ms

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
    consequent = []
    consequent_len = 0
    queue = deque([x])
    while queue:
        z = queue.popleft()
        if z in proposition.keys():
            for v in proposition[z]:
                if v not in consequent and v != x:
                    consequent.append(v)
                    queue.append(v)
                    consequent_len += 1
    return consequent, consequent_len

answer = defaultdict(list)
cnt = 0

for k in proposition.keys():
    consequent, consequent_len = bfs(k)
    answer[k] = sorted(consequent)
    cnt += consequent_len

print(cnt)
for k in sorted(proposition.keys()):
    for x in answer[k]:
        print(f"{k} => {x}")