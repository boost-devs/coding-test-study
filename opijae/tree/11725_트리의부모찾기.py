import sys
from collections import defaultdict

input= sys.stdin.readline
n = int(input())
graph_dict=defaultdict(list) # 노드들이 저장될 dict
parent = [0 for _ in range(n+1)] # 부모 정보가 저장될 list

for _ in range(n - 1):
    s,e=map(int,input().split())
    graph_dict[s].append(e) # 쌍방으로 값 넣어 주기
    graph_dict[e].append(s)

def dfs(graph_list, start, parent):
    stack = [start]
    while stack:
        node = stack.pop() # 부모 노드
        for i in graph_list[node]:
            parent[i]=node 
            stack.append(i) #자식 노드 넣기
            graph_list[i].remove(node)
    return parent

for i in list(dfs(graph_dict, 1, parent))[2:]:
    print(i)