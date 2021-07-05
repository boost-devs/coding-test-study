# https://www.acmicpc.net/problem/10844
# 쉬운 계단 수
# 29200 KB / 68 ms


N = int(input())

table = [[0] + [1] * 9]
for i in range(1, N):
    table.append([
        table[i - 1][1],
        *[
            table[i - 1][k - 1] + table[i - 1][k + 1]
            for k in range(1, 9)
        ],
        table[i - 1][8],
    ])

print(sum(table[-1]) % int(1e9))
