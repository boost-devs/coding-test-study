###### 9465번: 스티커
# https://www.acmicpc.net/problem/9465
# 메모리/시간: 47576KB / 1532ms

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    _map = tuple(tuple(map(int, input().split())) for _ in range(2))
    table = [[0 for _ in range(n)] for _ in range(2)]
    
    table[0][0] = _map[0][0]
    table[1][0] = _map[1][0]
    table[0][1] = table[1][0] + _map[0][1]
    table[1][1] = table[0][0] + _map[1][1]

    for i in range(2, n):
        table[0][i] = max(table[1][i-1]+_map[0][i], max(table[0][i-2], table[1][i-2])+_map[0][i])
        table[1][i] = max(table[0][i-1]+_map[1][i], max(table[0][i-2], table[1][i-2])+_map[1][i])

    print(max(max(table[0]), max(table[1])))