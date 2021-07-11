import sys
from collections import defaultdict,deque
input = sys.stdin.readline
n,m,k,x=map(int, input().split())
graph =defaultdict(list)
for _ in range(m):
    s,e=map(int,input().split())
    graph[s].append(e)
q=deque([[x,k]]) # 큐는 (시작 노드, 남은 거리) 가 저장된다.
visited=[False]*n
visited[x-1]=True
answer=[]
while q:
    start,remain=q.popleft()
    if remain<1:
        break
    for i in graph[start]:
        if not visited[i-1]: # index 맞춰주기 위해 -1
            visited[i-1]=True
            if remain-1==0: # 다음 남은 거리가 0이면 answer.append
                answer.append(i)
            q.append([i,remain-1])
if len(answer)==0:
    print(-1)
else:
    for i in sorted(answer):
        print(i)