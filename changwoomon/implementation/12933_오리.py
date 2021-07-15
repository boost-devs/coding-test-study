###### 12933번: 오리
# https://www.acmicpc.net/problem/12933
# 메모리/시간: 32076KB / 632ms

import sys
from collections import defaultdict

input = sys.stdin.readline

duck = input().rstrip()

def duckduck(duck):
    duck_queue = defaultdict(str)
    duck_idx = defaultdict(int)
    quack = "quack"

    for x in duck:
        k = 1
        while True:
            if x == quack[duck_idx[k]]:
                duck_queue[k] += x
                duck_idx[k] += 1
                break
            if not duck_queue.keys():
                return -1
            if max(duck_queue.keys()) < k:
                return -1
            k += 1
        for kk in duck_queue.keys():
            if duck_queue[kk] == "quack":
                duck_queue[kk] = ""
                duck_idx[kk] = 0

    for x in duck_queue.values():
        if x != "":
            return -1

    return max(duck_queue.keys())

print(duckduck(duck))