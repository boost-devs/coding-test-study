# https://www.acmicpc.net/problem/1106
# 호텔
# 29200 KB / 76 ms


def readline():
    return map(int, input().split())

C, N = readline()
INF = int(1e9)

info = []
for _ in range(N):
    cost, cust = readline()
    info.append((cost, cust))

info.sort(key=lambda p: p[0] / p[1])
table = [0, min(info)[0]]
for target in range(2, C + 1):
    table.append(min(
        cost + table[target - cust] if cust < target else cost
        for cost, cust in info
    ))

print(table[C])