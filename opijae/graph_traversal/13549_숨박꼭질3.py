# https://www.acmicpc.net/problem/13549

# 참고 https://goodlucknua.tistory.com/33

from collections import deque

def bfs():
    q=deque([n])

    while q:
        x=q.popleft()
        if x==k:
            return arr[x] 
        # -1,+1,*2 순으로 arr에 저장
        for nx in (x-1,x+1,2*x): # 순서에 따라 답이 될수도, 틀릴 수도 있음 1*2 == 1+1
            if 0<=nx<MAX and not arr[nx]:
                if nx==2*x and x!=0:
                    q.appendleft(nx) # *2일때가 최소 비용이니 우선순위의 최대로
                    arr[nx]=arr[x]
                else:
                    arr[nx]=arr[x]+1
                    q.append(nx)
n,k=map(int,input().split())
MAX=100001 # 최대 범위 정하기
arr = [0] * MAX # 각점마다 도달 시간을 저장하는 배열
print(bfs())