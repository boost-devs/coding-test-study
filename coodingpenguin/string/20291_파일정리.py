# 문제: [BOJ 20291] 파일 정리
# 유형: defaultdict, 정렬
# 메모리/시간: 45036kb / 300ms

import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
counter = defaultdict(int)

for _ in range(n):
    _, file_ext = input().rstrip().split(".")
    counter[file_ext] += 1

for ext, count in sorted(counter.items()):
    print(ext, count)
