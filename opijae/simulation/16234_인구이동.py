import sys
from collections import deque
input = sys.stdin.readline

n,l,r = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))
trans = [] # 인구 이동을 했을때 인구 수가 담기는 배열
answer = 0
direction = [(0, 1), (1,0),(0,-1),(-1,0)]
while True:
    visited = [[False] * n for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                q = deque([(i,j)])
                visited[i][j] = True
                _sum = arr[i][j] # 현재 sum 저장
                trans = [(i,j)] # 인구 이동할꺼에  저장
                while q:
                    cur_i,cur_j = q.popleft()
                    for di,dj in direction:
                        ni = cur_i + di
                        nj = cur_j + dj
                        if 0<= ni < n and 0 <= nj < n and not visited[ni][nj]:
                            if l <= abs(arr[cur_i][cur_j] -  arr[ni][nj]) <= r: # l,r 범위안에 들어 있음 인구이동함
                                visited[ni][nj] = True
                                q.append((ni, nj))   # 큐에 넣고
                                trans.append((ni, nj)) # 인구이동 배열에 넣음
                                _sum += arr[ni][nj] # sum 구하기
                if len(trans) > 1:  #인구 이동을 했으니
                    flag = True
                    for x,y in trans:
                        arr[x][y] = _sum//len(trans)  # 평균값 넣기
    if flag:
        answer += 1
    else:
        break
print(answer)