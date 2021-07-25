import sys
from collections import defaultdict
input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
n = int(input())
arr = [[0]*n for _ in range(n)]
like_dict = defaultdict(list)
result = 0
 
for _ in range(n*n):
    l = list(map(int, input().split()))
    like_dict[l[0]] = l[1:]
    
    # 조건 1&2 , 조건 3은 x가 돌고 y가 돌기 떄문에 y>=x
    max_x = 0 # 좋아하는 사람이 많은 x
    max_y = 0 # 좋아하는 사람이 많은 y
    max_like = -1 # 좋아하는 사람 수
    max_empty = -1 # 빈칸 수
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                like_cnt = 0
                empty_cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if arr[nx][ny] in l:
                            like_cnt += 1
                        if arr[nx][ny] == 0:
                            empty_cnt += 1
                            
                if max_like < like_cnt or (max_like == like_cnt and max_empty < empty_cnt):
                    max_x = i
                    max_y = j
                    max_like = like_cnt
                    max_empty = empty_cnt
                    
    arr[max_x][max_y] = l[0]
    
for i in range(n):
    for j in range(n):
        cnt = 0
        like = like_dict[arr[i][j]]
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] in like:
                    cnt += 1
        if cnt != 0:
            result += 10 ** (cnt-1)
            
print(result)