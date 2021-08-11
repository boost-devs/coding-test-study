# https://www.acmicpc.net/problem/16937
# 31312 KB / 96 ms


from itertools import permutations
from math import prod


def check(wi, wj, hi, hj, H, W):
    if (wi + wj <= W and max(hi, hj) <=H or
        max(wi, wj) <= W and hi + hj <= H):
        return True
    return False


H, W = map(int, input().split())
N = int(input())
stickers = [tuple(map(int, input().split())) for _ in range(N)]

max_area = 0
for i, j in permutations(range(N), 2):
    sum_area = prod(stickers[i]) + prod(stickers[j])
    if sum_area > H * W:
        continue
    ri, ci = stickers[i]
    rj, cj = stickers[j]
    pairs = [(ri, rj), (ri, cj), (ci, rj), (ci, cj)]
    for p in range(len(pairs)):
        wi, wj = pairs[p]
        hi, hj = pairs[-(p + 1)]
        if check(wi, wj, hi, hj, H, W):
            max_area = max(max_area, sum_area)
            break

print(max_area)
