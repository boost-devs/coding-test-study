# 문제: [BOJ 20291] 파일 정리
# 유형: defaultdict, 정렬
# 메모리/시간: 45036kb / 300ms

import sys
from collections import defaultdict

input = sys.stdin.readline

# 입력
n = int(input())  # 파일 개수
counter = defaultdict(int)  # 카운터

for _ in range(n):
    _, file_ext = input().rstrip().split(".")
    counter[file_ext] += 1  # 파일 확장자 개수 세기

# 이름으로 정렬 후, 출력
for ext, count in sorted(counter.items()):
    print(ext, count)
