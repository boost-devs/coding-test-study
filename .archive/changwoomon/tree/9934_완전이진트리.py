###### 9934번: 완전 이진 트리
# https://www.acmicpc.net/problem/9934
# 메모리/시간: 29200KB / 68ms

import sys

input = sys.stdin.readline

K = int(input())

node = list(map(int, input().split()))
node.insert(0, 0)
tree = [[] for _ in range(K)]

for i in range(K-1, -1, -1):
    j = 2**i
    tmp = []
    while j < len(node):
        if node[j] != 0:
            tree[i].append(node[j])
            node[j] = 0
        j += 2**i

for i in range(K-1, -1, -1):
    print(" ".join(map(str, tree[i])))