# https://www.acmicpc.net/problem/14467
# 소가 길을 건너간 이유 1
# 29200 KB / 76 ms


n = int(input())
counter = [[0, -1] for _ in range(10)] # (count, pos)
for _ in range(n):
    cow, pos = map(int, input().split())
    prev = counter[cow - 1]
    if prev[1] != pos:
        if prev[1] != -1:
            prev[0] += 1
        prev[1] = pos

print(sum(c for c, _ in counter))
