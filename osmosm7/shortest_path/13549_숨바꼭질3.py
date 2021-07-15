from collections import deque
import sys

st, end = map(int,input().split())

if st == end:
    print(0)
    sys.exit()
lst = [-1] * (200001)
step = 0
lst[st] = 0
nexts = deque([])
nexts.append(st)

while nexts:
    now = nexts.popleft()
    
    if now *2 in range(200000) and lst[now *2] == -1:
        lst[now *2] = lst[now] 
        nexts.appendleft(now *2)
    
    if now +1 in range(200000) and lst[now+1] == -1:
        lst[now+1] = lst[now]+1
        nexts.append(now + 1)
    
    if now -1 in range(200000) and lst[now-1] == -1:
        lst[now-1] = lst[now]+1
        nexts.append(now - 1)
    
    if lst[end] != -1:
        break
print(lst[end])
#print(nexts.count(end))