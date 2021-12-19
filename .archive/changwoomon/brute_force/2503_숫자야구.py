###### 2503번: 숫자 야구
# https://www.acmicpc.net/problem/2503
# 메모리/시간: 29200KB / 80ms

import sys

input = sys.stdin.readline

N = int(input())

baseball = [input().rstrip().split() for _ in range(N)]

cand = set()

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if (i==j) or (j==k) or (k==i):
                continue
            cand.add(str(i)+str(j)+str(k))

def play(cand, num, strike_n, ball_n):
    s = set()
    for c in cand:
        strike_cnt = 0
        ball_cnt = 0
        for i, x in enumerate(c):
            if x == num[i]:
                strike_cnt += 1
            if x in num[:i]+num[i+1:]:
                ball_cnt += 1
        if str(strike_cnt) != strike_n:
            s.add(c)
        if str(ball_cnt) != ball_n:
            s.add(c)
    return cand.difference(s)

for num, s, b in baseball:
    cand = play(cand, num, s, b)

print(len(cand))