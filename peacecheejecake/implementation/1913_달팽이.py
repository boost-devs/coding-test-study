# https://www.acmicpc.net/problem/1913
# 달팽이
# 67980 KB / 740 ms


n = int(input())
m = int(input())

table = [[0] * n for _ in range(n)]
for i in range(n):
    num = n ** 2 - i
    table[i][0] = num
    if num == m:
        the_coord = f"{i + 1} 1"

i, j = n // 2, n // 2
di, dj = -1, 0
num = 1
for stride in range(1, n):
    for _ in range(2):
        for _ in range(stride):
            table[i][j] = num
            if num == m:
                the_coord = f"{i + 1} {j + 1}"
            i, j = i + di, j + dj
            num += 1
        di, dj = dj, -di

for row in table:
    print(' '.join(map(str, row)))
print(the_coord)
