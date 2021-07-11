###### 11727번: 2×n 타일링 2
# https://www.acmicpc.net/problem/11727
# 메모리/시간: 32040KB / 88ms

import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())

def tiling(n):
    table = defaultdict(int)
    table[0] = 1
    for i in range(1, n+1):
        table[i] = table[i-1] + table[i-2]*2
    return table[n]

print(tiling(n) % 10007)