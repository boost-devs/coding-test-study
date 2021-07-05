# https://www.acmicpc.net/problem/2293
# 동전 1
# 29452 KB / 248 ms


n, k  = map(int, input().split())
coins = []
for _ in range(n):
    coin = int(input())
    if coin <= k:
        coins.append(coin)

table = [1] + [0] * k
for coin in coins:
    for tgt in range(coin, k + 1):
        table[tgt] += table[tgt - coin]

print(table[k])
