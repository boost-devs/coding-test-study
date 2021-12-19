###### 17073번: 나무 위의 빗물
# https://www.acmicpc.net/problem/17073
# 메모리/시간: 73304KB / 916ms

import sys
from collections import defaultdict

input = sys.stdin.readline

N, W = map(int, input().split())

tree = defaultdict(int)

for _ in range(N-1):
    U, V = map(int, input().split())
    tree[U] += 1
    tree[V] += 1

leaf_node = 0

for u, v in tree.items():
    if (u != 1) and (v == 1):
        leaf_node += 1

print(W / leaf_node)