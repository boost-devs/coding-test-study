# https://www.acmicpc.net/problem/20291
# 파일 정리
# 43524 KB / 304 ms

from collections import Counter
import sys

def input():
    return sys.stdin.readline().strip()

n = int(input())
extensions = [input().split('.')[1] for _ in range(n)]
counter = Counter(extensions)
for ext in sorted(counter):
    print(f"{ext} {counter[ext]}")
