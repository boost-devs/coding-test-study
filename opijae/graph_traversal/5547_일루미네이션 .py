# https://www.acmicpc.net/problem/5547
import sys
from collections import  deque

def bfs():
    q=deque([[0,0]])
    global cnt

    while q:
        i,j=q.popleft()

        visited[i][j]=True
        for di,dj in directions:
            if i%2==0 and di*dj!=0: # 이 문제는 다른 문제처럼 사각형으로 보는 것이 아닌 육각형으로 보기 때문에 홀,짝 열에 따라 특정 값을 바꿔 줘야된다.
                di*=-1
                dj*=-1
            ni=i+di
            nj=j+dj
            if (0 <= ni < h + 2) and (0 <= nj < w + 2):  # 안해주면 패딩 한 부분도 0 체크를 하기 때문에 필요
                if sangeun[ni][nj]=='1': # 0 옆이 1이면 cnt++
                    cnt+=1
                if sangeun[ni][nj]=='0' and not visited[ni][nj]: # 0옆이 0이면 큐에 추가
                    visited[ni][nj]=True
                    q.append([ni,nj])

input=sys.stdin.readline

w,h=map(int,input().split())

sangeun=[['0' for _ in range(w+2)]]
for _ in range(h):
    line=input().split()
    line.insert(0,'0')
    line.append('0')
    sangeun.append(line)
sangeun.append(['0' for _ in range(w+2)])

directions=[[-1,0],[0,1],[1,0],[0,-1],[1,1],[-1,1]]

cnt=0
visited = [[False] * (w + 2) for _ in range(h + 2)]
bfs()
print(cnt)