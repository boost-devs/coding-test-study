import sys
from collections import deque
input = sys.stdin.readline

n,m=map(int,input().split())

directions=[-1,1]
# max_num=100000001
# min_num=-100000001
q=deque([])
s=set([])
for ipt in input().split():
    q.append((int(ipt),0))
    s.add(int(ipt))  # 방문 한 지역 list로 check하면 시간 초과 났다.
def bfs():
    bulhang=0
    global m
    while q:
        len_q=len(q)
        for _ in range(len_q):
            sam,dist=q.popleft()
            for d in directions:
                n_sam=sam+d
                # if min_num < n_sam < max_num and n_sam not in s: https://www.acmicpc.net/board/view/56145 아니;; 집 범위 있는거 아니였냐구...
                if  n_sam not in s:  # 집이나 샘이 없다면 
                    m-=1  # 지어야 될 집개수 --
                    bulhang+=(dist+1)
                    if m==0:
                        return bulhang
                    q.append((n_sam,dist+1))
                    s.add(n_sam)
print(bfs())