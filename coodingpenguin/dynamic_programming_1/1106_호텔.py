# 문제: [BOJ 1106] 호텔
# 유형: 동적계획법
# 메모리/시간: 29200kb / 72ms
# 참고: https://dirmathfl.tistory.com/379

import sys

input = sys.stdin.readline
inf = int(1e9)

c, n = map(int, input().split())    # 최소 고객수, 도시 개수
arr = [list(map(int, input().split())) for _ in range(n)]   # 도시별 비용, 고객증가수
table = [0] + [inf] * (c+100)   # 테이블 (0은 꼭 0!)

for cost, pnum in arr:
    for i in range(pnum, c+101):
        table[i] = min(table[i], table[i-pnum] + cost) 

print(min(table[c:c+101]))  # 적어도 C명을 늘리기 위해 투자해야하는 최소값