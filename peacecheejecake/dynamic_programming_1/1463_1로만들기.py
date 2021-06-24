# https://www.acmicpc.net/problem/1463
# 1로 만들기
# 37012 KB / 1060 ms


n = int(input())
table = [0] * (n + 1)

for k in range(2, n + 1):
    cands = [k - 1]
    if k % 3 == 0:
        cands.append(k // 3)
    if k % 2 == 0:
        cands.append(k // 2)

    table[k] = min(table[c] for c in cands) + 1

print(table[-1])