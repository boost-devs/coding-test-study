import sys
from collections import deque
input = sys.stdin.readline
n,m,k = map(int, input().split())
arr = [[deque([]) for _ in range(n)] for _ in range(n)]
pointers = []
directions = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

for _ in range(m):
    _r,_c,_m,_s,_d = map(int, input().split())
    arr[_r-1][_c-1].append([_m,_s,_d])
    pointers.append((_r-1 ,_c-1))
# print(*arr,sep='\n')
for _ in range(k):
    for i,j in pointers:
        _m,_s,_d = arr[i][j].popleft()
        ni = i + directions[_d][0] * _s
        nj = j + directions[_d][1] * _s
        if 0<=ni <n and 0<=nj <n:
            arr[ni][nj].append([_m,_s,_d])

    pointers = []
    for i in range(n):
        for j in range(n):
            if len(arr[i][j])>1:
                _m_sum = 0
                _s_sum = 0
                direction_flag = True
                direction_num = 2
                for _m,_s,_d in arr[i][j]:
                    _m_sum += _m
                    _s_sum += _s
                    if direction_num ==2:
                        direction_num = _d%2
                    else:
                        if direction_num != _d%2:
                            direction_flag = False
                if direction_flag:
                    move_directions = [0,2,4,6]
                else:
                    move_directions = [1,3,5,7]
                _m = _m_sum // 5
                _s = _s_sum // len(arr[i][j])
                if _m ==0:
                    continue
                for d_idx in move_directions:
                    ni = i + directions[d_idx][0]
                    nj = j + directions[d_idx][1]
                    # print(ni, nj)
                    if ni <n and nj <n:
                        arr[ni][nj].append([_m,_s,d_idx])
                    if ni == -1:
                        ni = n-1
                    if nj == -1:
                        nj = n-1
                    pointers.append((ni,nj))
                arr[i][j] = deque()
print(*arr,sep='\n')
