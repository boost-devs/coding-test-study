# https://www.acmicpc.net/problem/11659
# 구간 합 구하기 4
# 39468 KB / 340 ms


import sys

def readline():
    return list(map(int, sys.stdin.readline().split()))

n, m = readline()
arr = readline()
sum_table = [0, arr[0]]
for i in range(2, len(arr) + 1):
    sum_table.append(sum_table[i - 1] + arr[i - 1])

for _ in range(m):
    i, j = readline()
    print(sum_table[j] - sum_table[i - 1])
