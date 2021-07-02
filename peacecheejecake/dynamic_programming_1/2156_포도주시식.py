# https://www.acmicpc.net/problem/2156
# 포도주 시식
# 30732 KB / 500 ms

n = int(input())

if n == 1:
    max_sum = int(input())
else:
    volumes = []
    for _ in range(n):
        volume = int(input())
        volumes.append(volume)

    table = [
        (volumes[0], volumes[0]), 
        (sum(volumes[:2]), volumes[1]),
        *([(0, 0)] * (n - 2)),
    ]
    for i in range(2, n):
        table[i] = (
            table[i - 1][1] + volumes[i],
            max(*table[i - 2], table[i - 3][0]) + volumes[i],
        )
    max_sum = max(table[-2][0], *table[-1])

print(max_sum)
