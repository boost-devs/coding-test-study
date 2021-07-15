import sys
import heapq
input = sys.stdin.readline
V,E= map(int, input().split()) 
arr=[[]for _ in range(V+1)]
k=int(input())
heap=[[0,k]] # 다음 탐색 노드 정보 저장
dist=[100000]*(V+1) # 출발지로 부터 정점까지의 거리
dist[k]=0

for _ in range(E):
    start,end,weight=map(int,input().split())
    arr[start].append([end,weight])

while heap:
    weight, node=heapq.heappop(heap) # 다음 노드 를 출발지로 설정
    for n_node,n_weight in arr[node]:
        if dist[n_node]>weight+n_weight: # 거리가 작으면
            dist[n_node]=weight+n_weight
            heapq.heappush(heap,[weight+n_weight,n_node]) # 다음 노드 후보군에 넣기

for i in range(1,V+1):
    if dist[i]==100000:
        print('INF')
    else:
        print(dist[i])