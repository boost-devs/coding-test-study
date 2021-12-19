###### 11726번: 2xn 타일링
# https://www.acmicpc.net/problem/11726
# 메모리/시간: 32040KB / 100ms

import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())

def tiling(n):
    table = defaultdict(int)
    table[1], table[2] = 1, 2
    for i in range(3, n+1):
        table[i] = table[i-1] + table[i-2]
    return table[n]

print(tiling(n) % 10007)