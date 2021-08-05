# https://www.acmicpc.net/problem/1969
# DNA
# 32056 KB / 104 ms


import sys
from collections import Counter


def input():
    return sys.stdin.readline().rstrip()


N, M = map(int, input().split())
dna_all = [input() for _ in range(N)]

min_dist_dna = ""
min_dist = 0
for column in zip(*dna_all):
    counter = Counter(column).most_common()
    counter.sort(key=lambda c: (-c[1], c[0]))
    min_dist_dna += counter[0][0]
    if len(counter) > 1:
        min_dist += sum(c for _, c in counter[1:])

print(min_dist_dna)
print(min_dist)
