import sys
from collections import deque
input = sys.stdin.readline
n=int(input())
arr=[]
for _ in range(n):
    temp=[]
    for i,j in enumerate(map(int,input().split())):
        if j==1: # 간선이 존재하는 경우 저장
            temp.append(i)
    arr.append(temp)
# bfs
for i in range(n):
    temp=[]
    q=deque([arr[i]])
    visited=[False]*n
    while q:
        indexs=q.popleft() # 간선이 존재하는 경우
        for index in indexs:
            if not visited[index]:
                visited[index]=True
                q.append(arr[index])
    temp=[]
    for check in visited: # 다른 노드\들을 방문했는지 확인
        if check:
            temp.append(1)
        else:
            temp.append(0)
    print(*temp)