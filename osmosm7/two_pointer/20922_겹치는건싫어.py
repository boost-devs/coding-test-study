n,k = map(int,input().split())
lst = list(map(int,input().split()))

lt = 0
check_lst = [0] * 200001
check_lst[lst[0]] += 1
max_len = 1
 

for i in range(1,n):
    now_num = lst[i]
    check_lst[now_num] +=1
    if check_lst[now_num] > k:
        # k개 이하로
        while check_lst[now_num] > k and lt < i:
            lt_num = lst[lt]
            check_lst[lt_num] = check_lst[lt_num] -1
            lt +=1
 
    now_len = i-lt+1
    if max_len < now_len:
        max_len = now_len

print(max_len)