# https://www.acmicpc.net/problem/11727
# 2xn 타일링 2
# 29200 KB / 84 ms

n = int(input())
table = [1, 1] + [0] * (n - 1)
for i in range(2, n + 1):
    table[i] = (2 * table[i - 2] + table[i - 1]) % 10007
print(table[-1])
