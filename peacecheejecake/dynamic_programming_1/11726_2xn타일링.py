# https://www.acmicpc.net/problem/11726
# 2xn 타일링
# 29200 KB / 68 ms

n = int(input())
table = [0, 1, 2] + [0] * (n - 2)

for i in range(3, n + 1):
    table[i] = (table[i - 1] + table[i - 2]) % 10007

print(table[n])
