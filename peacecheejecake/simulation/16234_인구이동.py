# https://www.acmicpc.net/problem/16234
# 139968 KB / 2204 ms (PyPy3)


from collections import deque


N, L, R = map(int, input().split())
populations = []
for _ in range(N):
    populations.append([int(x) for x in input().split()])

num_moves = 0
while True:
    visited = [[False] * N for _ in range(N)]
    moved = False
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue

            visited[i][j] = True
            queue = deque([(i, j)])
            union = {(i, j)}
            adj_dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            while queue:
                ib, jb = queue.popleft()
                for di, dj in adj_dirs:
                    ni, nj = ib + di, jb + dj
                    if (ni < 0 or ni >= N or nj < 0 or nj >= N or
                        visited[ni][nj]):
                        continue

                    diff = abs(populations[ni][nj] - populations[ib][jb])
                    if diff >= L and diff <= R:
                        visited[ni][nj] = True
                        queue.append((ni, nj))
                        union.add((ni, nj))

            if len(union) > 1:
                union_sum = sum(populations[iu][ju] for iu, ju in union)
                union_dis = union_sum // len(union)
                for iu, ju in union:
                    populations[iu][ju] = union_dis
                moved = True
    
    # check if moved
    if moved:
        num_moves += 1
    else:
        break

print(num_moves)
