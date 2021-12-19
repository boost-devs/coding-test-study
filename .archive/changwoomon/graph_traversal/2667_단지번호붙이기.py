###### 2667번: 단지번호붙이기
# https://www.acmicpc.net/problem/2667
# 메모리/시간: 29136KB / 68ms

import sys

input = sys.stdin.readline

N = int(input())

_map = [list(map(int, input().rstrip())) for _ in range(N)] # rstrip() 안해주면 error

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def dfs(x, y, cluster):
    if (x < 0) or (x >= N) or (y < 0) or (y >= N):
        return False
    
    if _map[x][y] == 1:
        cluster.append([x, y])
        _map[x][y] = 0

        for way in range(4):
            xx, yy = x + dx[way], y + dy[way]
            dfs(xx, yy, cluster)

        return True

    return False

cnt = 0
num_cluster = []

for i in range(N):
    for j in range(N):
        cluster = []

        if dfs(i, j, cluster) == True:
            cnt += 1
            num_cluster.append(len(cluster))

print(cnt)
num_cluster.sort()
print("\n".join(map(str, num_cluster)))