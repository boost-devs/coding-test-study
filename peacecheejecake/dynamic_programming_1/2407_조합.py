# https://www.acmicpc.net/problem/2407
# 조합
# 29200 KB / 72 ms

n, m = map(int, input().split())
table = [1]
for i in range(1, n + 1):
    table.append(table[i - 1] * i)

print(table[n] // table[m] // table[n - m])
