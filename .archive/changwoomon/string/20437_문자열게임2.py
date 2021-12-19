###### 20437번: 문자열 게임 2
# https://www.acmicpc.net/problem/20437
# 메모리/시간: 32156KB / 276ms

import sys
from collections import deque, Counter, defaultdict

input = sys.stdin.readline

T = int(input())

def str_game(dict):
    global K
    length = deque([-1])
    for k, v in dict.items():
        if len(v) >= K:
            for i in range(len(v)-K+1):
                length.append(v[i+K-1] - v[i] + 1)
    return length

for i in range(T):
    W = input().rstrip()
    K = int(input().rstrip())
    c = Counter(W)
    if max(c.values()) < K:
        print(-1)
        continue
    d = defaultdict(list)
    for i, x in enumerate(W):
        d[x].append(i)
    game = str_game(d)
    if len(game) == 1:
        print(-1)
    else:
        game.popleft()
        print(f"{min(game)} {max(game)}")
