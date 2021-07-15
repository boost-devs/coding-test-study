import sys
input = sys.stdin.readline

n,w=map(int,input().split())
if n==1:
    print(w) # 노드가 한개면 W print
else:
    node= [0]*(n+1) # 노드가 저장될 배열
    for _ in range(n - 1):
        u,v=map(int, input().split())
        # 자식 노드가 있는지 판별
        if node[u]<2:
            node[u]+=1
        if node[v]<2:
            node[v]+=1
    cnt=0
    # 1번 노드 제외하기
    for v in node[2:]:
        if v==1: # 자식 노드들 개수 세기
            cnt+=1
    print(w/cnt)