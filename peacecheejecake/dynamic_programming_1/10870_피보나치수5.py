# https://www.acmicpc.net/problem/10870
# 피보나치 수 5
# 29200 KB / 68 ms


prev, curr = -1, 1
for _ in range(int(input()) + 1):
    prev, curr = curr, prev + curr

print(curr)