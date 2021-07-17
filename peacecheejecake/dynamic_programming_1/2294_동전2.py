# https://www.acmicpc.net/problem/2294
# 동전 2
# 29452 KB / 448 ms


INF = 1000001

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coin = int(input())
    if coin not in coins:
        coins.append(coin)

table = [0] + [INF] * k
for coin in coins:
    for tgt in range(coin, k + 1):
        table[tgt] = min(table[tgt], table[tgt - coin] + 1)

if table[k] < INF:
    print(table[k])
else:
    print(-1)
