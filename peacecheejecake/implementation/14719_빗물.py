# https://www.acmicpc.net/problem/14719
# 빗물
# 29592 KB / 88 ms


h, w = map(int, input().split())
blocks = [['0'] * w for _ in range(h)]
for c, col in enumerate(map(int, input().split())):
    for r in range(col):
        blocks[r][c] = '1'

volume = 0
for row in blocks:
    volume += ''.join(row).strip('0').count('0')

print(volume)
