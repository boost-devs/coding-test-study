from collections import deque
import sys

n,m = map(int,sys.stdin.readline().split())

mat = [deque([0]*20) for _ in range(n)]

for _ in range(m):
    inpt = list(map(int,sys.stdin.readline().split()))
    if inpt[0] < 3:
        num,i,idx = inpt
    else:
        num,i = inpt
    
    if num == 1:
        mat[i-1][idx-1] = 1
    if num == 2:
        mat[i-1][idx-1] = 0
    if num ==3:
        mat[i-1].appendleft(0)
        mat[i-1].pop()
    if num ==4:
        mat[i-1].popleft()
        mat[i-1].append(0)

lst = []
for i in range(n):
    if ''.join(list(map(str,mat[i]))) in lst:
        continue
    lst.append(''.join(list(map(str,mat[i]))))

print(len(lst))