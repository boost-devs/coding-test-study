import sys

input = sys.stdin.readline
n, m = map(int, input().split())
train = [[0] * 20 for _ in range(n)]

for _ in range(m):
    order = list(map(lambda x: x - 1, map(int, input().split()))) # -1 적용해 저장
    if order[0] == 0:
        train[order[1]][order[2]] = 1
    elif order[0] == 1:
        train[order[1]][order[2]] = 0
    elif order[0] == 2:
        train[order[1]] = train[order[1]][:19] # rotate
        train[order[1]].insert(0, 0)
    elif order[0] == 3:
        train[order[1]] = train[order[1]][1:] # rotate
        train[order[1]].append(0)
arr = []
cnt = 0
for tr in train:
    if tr not in arr:
        cnt += 1
        arr.append(tr)
print(cnt)
