import sys
from collections import deque
def bfs(q,data):
    while q:
        x,y= q.popleft()
        data[x][y] = '.'
        for d in directions:
            nx,ny = x+d[0],y+d[1]
            if 0<=nx<r and 0<=ny<c and data[nx][ny]=='O':
                data[nx][ny] = '.'

input=sys.stdin.readline
r,c,n = map(int,input().split())
data = [list(input()) for _ in range(r)]
directions=[[0,1],[-1,0],[1,0],[0,-1]]
q = deque()

for idx in range(1,n+1):

    if idx == 1: # 1일때는 아무것도 안하고 폭탄 위치만 가져온다.
        for i in range(r):
            for j in range(c):
                if data[i][j] == 'O':
                    q.append((i,j))
    elif idx % 2 == 1:
        bfs(q,data)
        for x in range(r): # 위에랑 변수명을 다르게 해줘야 bfs 들어갔을때 안꼬인다.
            for y in range(c):
                if data[x][y] == 'O':
                    q.append((x,y))
    else:
        data = [['O']*c for _ in range(r)] # 규칙을 보면 짝수 번째일때는 전부 폭탄이다.

for row in data:
    print(''.join(row))