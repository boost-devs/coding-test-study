###### 10798번: 세로읽기
# https://www.acmicpc.net/problem/10798
# 메모리/시간: 29200KB / 68ms

import sys

input = sys.stdin.readline

_input = [list(map(str, input().rstrip())) for _ in range(5)]

_max = 0

for i in range(5):
    if len(_input[i]) > _max:
        _max = len(_input[i])

answer = ""

for j in range(_max):
    for i in range(5):
        try:
            answer += _input[i][j]
        except:
            continue

print(answer)