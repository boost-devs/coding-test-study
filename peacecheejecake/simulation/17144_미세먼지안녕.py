# https://www.acmicpc.net/problem/17144
# 127080 KB / 412 ms (PyPy3)


R, C, T = map(int, input().split())
room, rps = [], []
for r in range(R):
    row = [int(x) for x in input().split()]
    room.append(row)
    if row[0] == -1:
        rps.append(r)

upper_coords = (
    [(rps[0], c) for c in range(1, C)]
    + [(r, -1) for r in range(rps[0] - 1, -1, -1)]
    + [(0, c) for c in range(C - 2, -1, -1)]
    + [(r, 0) for r in range(1, rps[0])]
)
lower_coords = (
    [(rps[1], c) for c in range(1, C)]
    + [(r, -1) for r in range(rps[1] + 1, R)]
    + [(-1, c) for c in range(C - 2, -1, -1)]
    + [(r, 0) for r in range(R - 2, rps[1], -1)]
)

adj_dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for t in range(T):
    # diffusion
    future_room = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if room[r][c] == 0 or room[r][c] == -1:
                continue

            diff_vol = room[r][c] // 5
            for dr, dc in adj_dirs:
                ra, ca = r + dr, c + dc
                if (ra < 0 or ra >= R or ca < 0 or ca >= C or
                    ca == 0 and ra in rps):
                    continue
                room[r][c] -= diff_vol
                future_room[ra][ca] += diff_vol

    for r in range(R):
        for c in range(C):
            room[r][c] += future_room[r][c]

    # purifiers
    upper_way = [room[r][c] for r, c in upper_coords]
    room[rps[0]][1] = 0
    for (r, c), bb in zip(upper_coords[1:], upper_way[:-1]):
        room[r][c] = bb
    
    lower_way = [room[r][c] for r, c in lower_coords]
    room[rps[1]][1] = 0
    for (r, c), bb in zip(lower_coords[1:], lower_way[:-1]):
        room[r][c] = bb

answer = sum(sum(row) for row in room) + 2
print(answer)
