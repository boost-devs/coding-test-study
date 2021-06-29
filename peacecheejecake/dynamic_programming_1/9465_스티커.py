# https://www.acmicpc.net/problem/9465
# 스티커 (DP)
# 58984 KB / 1268 ms


import sys

readline = sys.stdin.readline


def get_single_input():
    n = int(readline())
    stickers = []
    for _ in range(2):
        stickers.append([int(x) for x in readline().split()])
    stickers = list(zip(*stickers))
    return n, stickers


def get_partial_max(max_table, column):
    prev_prev, prev = max_table[-2:]
    upper, lower = column

    upper += max(max(prev_prev), prev[1]) # 선택 안함 vs 아래 선택
    lower += max(max(prev_prev), prev[0]) # 선택 안함 vs 위 선택
    return (upper, lower)


T = int(readline())

for _ in range(T):
    n, stickers = get_single_input()    

    max_0 = stickers[0]
    max_1 = (
        stickers[0][1] + stickers[1][0], 
        stickers[0][0] + stickers[1][1],
    )
    max_table = [max_0, max_1]
    for i in range(2, n):
        max_table.append(
            get_partial_max(max_table, stickers[i])
        )
    max_score = max(max_table[-1])
    
    print(max_score)
