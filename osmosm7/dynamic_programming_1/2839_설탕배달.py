import sys
n = int(input())
if n == 3 or n ==5:
    print(1)
    sys.exit()
if n ==4:
    print(-1)
    sys.exit()
    
lst = [-1] * (n+1)
lst[3] = 1
lst[5] = 1

for i in range(6,n+1):
    if lst[i-3] != -1 and lst[i-5] !=-1:
        lst[i] = min(lst[i-3],lst[i-5]) + 1
    elif lst[i-3] != -1:
        lst[i] = lst[i-3] +1
    elif lst[i-5] != -1:
        lst[i] = lst[i-5] +1

print(lst[-1])