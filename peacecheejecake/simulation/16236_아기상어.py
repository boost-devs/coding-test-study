# https://www.acmicpc.net/problem/16236
# 31956 KB / 96 ms


from collections import deque


N = int(input())
space = []
for r in range(N):
    row = []
    for c, x in enumerate(input().split()):
        if x == '9':
            rs, cs = r, c
            row.append(0)
        else:
            row.append(int(x))
    space.append(row)

INF = N ** 2 + 1
adj_dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]

size = 2
_count = 0
time = 0
while True:
    distances = [[INF] * N for _ in range(N)]
    distances[rs][cs] = 0
    min_distance = INF
    cands = set()
    queue = deque([(rs, cs)])
    while queue:
        r, c = queue.popleft()
        distance = distances[r][c]
        if distance >= min_distance:
            break

        for dr, dc in adj_dirs:
            rn, cn = r + dr, c + dc
            if rn >= 0 and rn < N and cn >= 0 and cn < N:
                if space[rn][cn] > 0 and space[rn][cn] < size:
                    cands.add((rn, cn))
                    min_distance = distance + 1
                elif space[rn][cn] <= size and distances[rn][cn] > distance + 1:
                    distances[rn][cn] = distance + 1
                    queue.append((rn, cn))
    
    if cands:
        rs, cs = min(cands)
        space[rs][cs] = 0
        time += min_distance
        _count += 1
        if _count == size:
            size += 1
            _count = 0
    else:
        break

print(time)
