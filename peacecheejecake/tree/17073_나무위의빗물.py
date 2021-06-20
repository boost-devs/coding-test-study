# https://www.acmicpc.net/problem/17073
# 나무 위의 빗물

import sys

def input():
    return sys.stdin.readline().strip()

N, W = map(int, input().split())
node_counts = {}
for _ in range(N - 1):
    u, v = map(int, input().split())
    node_counts[u] = node_counts.get(u, 0) + 1
    node_counts[v] = node_counts.get(v, 0) + 1

num_leaves = len([
    node for node, count in  node_counts.items() 
    if node != 1 and count == 1
])

print(f"{W / num_leaves}")