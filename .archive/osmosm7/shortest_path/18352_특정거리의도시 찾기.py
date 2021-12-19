import sys
from collections import defaultdict,deque
input = sys.stdin.readline
n,m,k,x = map(int,input().split())
adj_lst = defaultdict(list)
for _ in range(m):
    a,b = map(int,input().split())
    adj_lst[a].append(b)
visit = [0] * (n+1)
visit[x] =1
dq = deque([])
dq.append(x)
step = 0
while dq:
    for _ in range(len(dq)):
        now = dq.popleft()
        for i in adj_lst[now]:
            if visit[i] == 0:
                visit[i] = 1
                dq.append(i)
    step+=1
    if step == k:
        break
        
if len(dq) == 0:
    print(-1)
else:
    dq = list(dq)
    dq.sort()
    for i in dq:
        print(i)
            