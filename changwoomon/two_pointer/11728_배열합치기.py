###### 11728번: 배열 합치기
# https://www.acmicpc.net/problem/11728
# 메모리/시간: 184056KB / 1512ms

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

array = []

for _ in range(2):
    array.extend(map(int, input().split()))

print(*sorted(array))