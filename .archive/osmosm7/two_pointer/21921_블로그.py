import sys
n,m = map(int,input().split())
lst = list(map(int,input().split()))
max_num = sum(lst[:m])
max_cnt = 1

if n == m:
    if max_num == 0:
        print('SAD')
    else:
        print(max_num)
        print(max_cnt)
    sys.exit()


now_num = sum(lst[:m])

for i in range(1,n-m+1):
    #now_num = sum(lst[i:i+m])
    now_num = now_num - lst[i-1] + lst[i+m-1]
    
    if max_num < now_num:
        max_num = now_num
        max_cnt = 1
    elif max_num == now_num:
        max_cnt += 1
    
if max_num == 0:
    print('SAD')
else:
    print(max_num)
    print(max_cnt)