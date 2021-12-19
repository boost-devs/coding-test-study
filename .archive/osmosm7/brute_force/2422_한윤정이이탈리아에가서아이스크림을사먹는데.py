import sys
from collections import defaultdict
#input = sys.stdin.readline


n,m = map(int,input().split())
no_dict = defaultdict(list)
for _ in range(m):
    
    a,b = map(int,input().split())
    no_dict[min(a,b)].append(max(a,b))

cnt = 0
for i in range(1,n-1):
    for j in range(i+1,n):
        if j in no_dict[i]:
            continue
        for k in range(j+1,n+1):
            if k in no_dict[i] or k in no_dict[j]:
                continue
            cnt+=1
print(cnt)