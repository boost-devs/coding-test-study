###### 20291번: 파일 정리
# https://www.acmicpc.net/problem/20291
# 메모리/시간: 42992KB / 244ms

import sys

input = sys.stdin.readline

N = int(input())

extension = dict()

for _ in range(N):
    ext = input().rstrip().split(".")[1]
    if ext not in extension.keys():
        extension[ext] = 1
    else:
        extension[ext] += 1

answer = sorted(extension.items(), key=lambda x: x[0])
for x in answer:
    k, v = x
    print(f"{k} {v}")