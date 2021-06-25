# https://www.acmicpc.net/problem/9095
# 1, 2, 3 더하기
# 29200 KB / 68 ms


import sys


def input():
    return sys.stdin.readline().strip()


def create_table(max_n):
    table = [0, 1, 2, 4]
    for _ in range(4, max_n + 1):
        num_cases = sum(table[-3:])
        table.append(num_cases)
    return table


table = create_table(10)
for _ in range(int(input())):
    print(table[int(input())])
