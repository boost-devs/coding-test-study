# https://www.acmicpc.net/problem/15686
# 29200 KB / 468 ms

from itertools import combinations

n, m = map(int, input().split())
homes, chickens = [], []
for i in range(n):
    for j, sym in enumerate(input().split()):
        if sym == '1':
            homes.append((i, j))
        elif sym == '2':
            chickens.append((i, j))

min_dist = 2 * n * len(homes)
for comb in combinations(chickens, m):
    dist = 0
    for i, j in homes:
        dist += min(map(lambda x: abs(x[0] - i) + abs(x[1] - j), comb))
    min_dist = min(min_dist, dist)

print(min_dist)
