# https://www.acmicpc.net/problem/2470
# 두 용액
# 42684 KB / 176 ms


import sys
from bisect import bisect


input = sys.stdin.readline

N = int(input())

acids = [] # positive
alkalis = [] # negative or zero
for prop in map(int, input().split()):
    if prop > 0:
        acids.append(prop)
    else:
        alkalis.append(prop)

acids.sort()
alkalis.sort()

cands = []
if len(acids) > 1:
    cands.append((sum(acids[:2]), tuple(acids[:2])))
if len(alkalis) > 1:
    cands.append((sum(alkalis[-2:]), tuple(alkalis[-2:])))

neut_pair = (int(2e9 + 1), None)
for acid in acids:
    if neut_pair[0] == 0:
        break

    idx = bisect(alkalis, -acid)
    if idx > 0:
        f = alkalis[idx - 1]
        if abs(acid + f) < abs(neut_pair[0]):
            neut_pair = (acid + f, (f, acid))
    if idx < len(alkalis):
        l = alkalis[idx]
        if abs(acid + l) < abs(neut_pair[0]):
            neut_pair = (acid + l, (l, acid))

cands.append(neut_pair)

_, pair = min(cands, key=lambda x: abs(x[0]))
print(' '.join(map(str, pair)))
