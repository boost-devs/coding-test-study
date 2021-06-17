import sys
input = sys.stdin.readline
n= int(input())
arr= [0]*(n+1) # 정점의 개수를 저장

for _ in range(n-1):
    s,e=map(int, input().split())
    arr[s]+=1 # 연결된 점 ++
    arr[e]+=1 # 연결된 점 ++

q=int(input())
for _ in range(q):
    t,k=map(int, input().split())
    if t==1:
        if arr[k]>1: # 연결된 점이 2개 이상이면 단절점
            print('yes')
        else:
            print('no')
    else: # t가 2일떄, 사이클이 없다 -> 양방향 이동 X -> 모든 간선이 단절선
        print('yes')