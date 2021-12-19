n = int(input())
lst = list(map(int,input().split()))

lst.sort()
lt = 0
rt = n-1
lt_num = lst[lt]
rt_num = lst[rt]

l_answer = lst[lt]
r_answer = lst[rt]

answer = abs(lt_num + rt_num)

while lt < rt:
    lt_num = lst[lt]
    rt_num = lst[rt]
    
    if answer > abs(lt_num + rt_num):
        answer = abs(lt_num + rt_num)
        l_answer = lst[lt]
        r_answer = lst[rt]

    if abs(lt_num) < abs(rt_num):
        rt -=1
    else:
        lt +=1
print(l_answer,r_answer)