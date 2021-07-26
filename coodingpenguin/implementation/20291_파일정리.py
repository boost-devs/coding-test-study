# 문제: [BOJ 20291] 파일 정리
# 유형: 구현, 카운터
# 메모리/시간: 42440kb / 256ms

import sys

input = sys.stdin.readline

n = int(input())  # 파일 개수
file_ext = {}  # 파일 확장자 카운터
for _ in range(n):
    name, ext = input().rstrip().split(".")  # 파일명, 확장자명
    # 없는 확장자라면 초기화
    if ext not in file_ext:
        file_ext[ext] = 1
    # 있는 확장자라면 개수 카운트
    else:
        file_ext[ext] += 1

# 이름 순으로 출력
for ext, count in sorted(file_ext.items()):
    print(ext, count)
