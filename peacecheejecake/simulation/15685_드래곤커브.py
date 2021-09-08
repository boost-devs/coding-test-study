# https://www.acmicpc.net/problem/15685
# 29452 KB / 92 ms


def update(x, y, d, g):
    global vertices, init_dirs
    dx, dy = init_dirs[d]
    curve = [(x, y), (x + dx, y + dy)]
    for _ in range(g):
        xa, ya = curve[-1]
        for xx, yy in curve[-2::-1]:
            curve.append((-yy + ya + xa, xx - xa + ya))
    vertices.update(set(curve))


vertices = set()
init_dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]

N = int(input())
for _ in range(N):
    update(*tuple(int(x) for x in input().split()))

num_squares = 0
for x, y in vertices:
    if ((x + 1, y) in vertices and (x, y + 1) in vertices and
        (x + 1, y + 1) in vertices):
        num_squares += 1
        
print(num_squares)
