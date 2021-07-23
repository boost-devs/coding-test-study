# https://www.acmicpc.net/problem/20207
# 달력
# 29200 KB / 176 ms


n = int(input())
calendar = [0] * 365
for _ in range(n):
    s, e = map(int, input().split())
    for i in range(s - 1, e):
        calendar[i] += 1

area = 0
h, w = 0, 0
for e in calendar:
    if e == 0:
        area += h * w
        h, w = 0, 0
    else:
        h += 1
        w = max(w, e)

if h > 0 and w > 0:
    area += h * w

print(area)
