# https://www.acmicpc.net/problem/14675
# 단절점과 단절선

import sys
def input():
    return sys.stdin.readline().strip()


num_nodes = int(input())
num_appearances = [0] * num_nodes
for _ in range(num_nodes - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    num_appearances[a] += 1
    num_appearances[b] += 1

num_queries = int(input())
for _ in range(num_queries):
    t, k = map(lambda x: int(x) - 1, input().split())
    if t == 1 or num_appearances[k] > 1:
        print("YES")
    else:
        print("NO")
