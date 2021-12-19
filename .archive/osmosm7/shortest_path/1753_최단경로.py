from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
start = int(input())
graph = defaultdict(list)

for _ in range(m):
    s,e,w = map(int,input().split())
    graph[s].append((e,w))
    
def daikstra(graph,V,start):
    
    Q = [(0,start)]
    distance = defaultdict(list)
    
    while Q:
        dist, node = heapq.heappop(Q)
        if node not in distance:
            distance[node] = dist
            for e,w in graph[node]:
                update = dist+w
                heapq.heappush(Q,(update,e))
    for i in range(1,1+V):
        if i ==start:
            print(0)
        elif i not in distance:
            print('INF')
        else:
            print(distance[i])
daikstra(graph,n,start)