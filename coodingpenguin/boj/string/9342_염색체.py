# 문제: [BOJ 9342] 염색체
# 유형: 문자열, 정규표현식
# 메모리/시간: 33020kb / 128ms

import sys
import re

input = sys.stdin.readline

t = int(input())  # 테스트 케이스 개수

# 정규식 패턴 정의
p = re.compile(r"^[ABCDEF]{0,1}A+F+C+[ABCDEF]{0,1}$")

for _ in range(t):
    chrom = input().rstrip()  # 염색체
    # 패턴과 일치한 경우
    if p.match(chrom):
        print("Infected!")
    # 일치하지 않는 경우
    else:
        print("Good")
