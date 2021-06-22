# https://www.acmicpc.net/problem/2748
# 피보나치 수 2
# 29200 KB / 76 ms


prev, curr = -1, 1
for _ in range(int(input()) + 1):
    prev, curr = curr, prev + curr

print(curr)