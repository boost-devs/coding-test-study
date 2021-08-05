###### 1969번: DNA
# https://www.acmicpc.net/problem/1969
# 메모리/시간: 32040KB / 116ms

import sys
from collections import Counter

input = sys.stdin.readline

N, M = map(int, input().split())

dna = [input().rstrip() for _ in range(N)]

answer = ""

for i in range(M):
    tmp = []
    for d in dna:
        tmp.append(d[i])
    c = Counter(tmp)
    answer += sorted(c.items(), key=lambda x: (-x[1], x[0]))[0][0]

hamming_distance = 0

for d in dna:
    for i, n in enumerate(d):
        if n != answer[i]:
            hamming_distance += 1

print(answer, hamming_distance, sep="\n")