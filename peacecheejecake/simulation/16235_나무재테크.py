# https://www.acmicpc.net/problem/16235
# 139108 KB / 528 ms (PyPy3)


N, M, K = map(int, input().split())
winter = [[int(x) for x in input().split()] for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x - 1][y - 1].append(z)
nours = [[5] * N for _ in range(N)]

adj_dirs = [
    (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
]

for _ in range(K):
    # spring & summer
    for r in range(N):
        for c in range(N):
            trees[r][c].sort()
            for i, age in enumerate(trees[r][c]):
                if nours[r][c] >= age:
                    nours[r][c] -= age
                    trees[r][c][i] += 1
                else:
                    nours[r][c] += sum(a // 2 for a in trees[r][c][i:])
                    trees[r][c] = trees[r][c][:i]
                    break

    # autumn & winter
    for r in range(N):
        for c in range(N):
            num_breed = len([age for age in trees[r][c] if age % 5 == 0])
            for dr, dc in adj_dirs:
                rn, cn = r + dr, c + dc
                if rn >= 0 and rn < N and cn >= 0 and cn < N:
                    trees[rn][cn].extend([1] * num_breed)
            nours[r][c] += winter[r][c]

num_trees = sum(sum(map(len, row)) for row in trees)
print(num_trees)
