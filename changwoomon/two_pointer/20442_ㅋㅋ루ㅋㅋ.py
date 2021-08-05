###### 20442번: ㅋㅋ루ㅋㅋ
# https://www.acmicpc.net/problem/20442
# 메모리/시간: 162576KB / 2288ms

import sys

input = sys.stdin.readline

zzfzz = input().rstrip()

lk = []
cnt = 0

for s in zzfzz:
    if s == "K":
        cnt += 1
    else:
        lk.append(cnt)

rk = []
cnt = 0

for s in zzfzz[::-1]:
    if s == "K":
        cnt += 1
    else:
        rk.append(cnt)

rk = rk[::-1]

left, right = 0, len(lk)-1

max_len = 0

while (left <= right):
    max_len = max(max_len, right-left+1+2*min(lk[left], rk[right]))
    if lk[left] < rk[right]:
        left += 1
    else:
        right -= 1

print(max_len)