###### 20291번: 파일 정리
# https://www.acmicpc.net/problem/20291
# 메모리/시간: 45688KB / 260ms

import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())

extension = Counter([input().rstrip().split('.')[1] for _ in range(N)])

answer = sorted(extension.items(), key=lambda x: x[0])

for k, v in answer:
    print(k, v)