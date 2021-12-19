###### 9095번: 1, 2, 3 더하기
# https://www.acmicpc.net/problem/9095
# 메모리/시간: 31824KB / 96ms

import sys
from collections import defaultdict

input = sys.stdin.readline

T = int(input())

def one_two_three(n):
    table = defaultdict(int)
    table[0] = 1
    
    for i in range(1, n+1):
        table[i] = table[i-1] + table[i-2] + table[i-3]
    
    return table[n]

for _ in range(T):
    n = int(input())
    print(one_two_three(n))