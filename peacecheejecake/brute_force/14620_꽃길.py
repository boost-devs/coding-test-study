# https://www.acmicpc.net/problem/14620
# 29200 KB / 308 ms


from itertools import combinations


N = int(input())
prices = []
for _ in range(N):
    prices.append([int(x) for x in input().split()])

min_price = 3000
for p1, p2, p3 in combinations(range(N, N * (N - 1)), 3):
    if p1 == p2 or p2 == p3 or p3 == p2:
        continue

    p1, p2, p3 = divmod(p1, N), divmod(p2, N), divmod(p3, N)
    if (
        all(p[1] > 0 and p[1] < N - 1 for p in (p1, p2, p3)) and
        all(
            abs(pi[0] - pj[0]) + abs(pi[1] - pj[1]) > 2 
            for pi, pj in combinations((p1, p2, p3), 2)
        )
    ):
        price = sum(
            prices[r][c] 
            + prices[r - 1][c] + prices[r + 1][c]
            + prices[r][c - 1] + prices[r][c + 1]
            for r, c in (p1, p2, p3)
        )
        min_price = min(min_price, price)

print(min_price)
