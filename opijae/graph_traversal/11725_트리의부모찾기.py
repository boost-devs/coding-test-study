import sys
from collections import deque,defaultdict

def bfs():
    q=deque([1])
    visited[1]=True
    while q:
        node=q.popleft()
        for i in graph_dict[node]:
            if visited[i]==False:
                q.append(i)
                visited[i]=True
                parent[i]=node  # 현재 node는 부모고 i는 node의 자식
input=sys.stdin.readline
n=int(input())
graph_dict=defaultdict(list) # defaultdict을 이용해 편하게 dict을 만들자
# visited=[False] * (n+1)
visited=[False for _ in range(n+1)]
# parent=[0]*(n+1)
parent=[0 for _ in range(n+1)]  # 부모 정보가 저장될 배열
for _  in range(n-1):
    s,e=map(int,input().split())
    graph_dict[s].append(e)
    graph_dict[e].append(s)
bfs()
# print(*parent[2:],sep='\n')
for i in parent[2:]:
    print(i)