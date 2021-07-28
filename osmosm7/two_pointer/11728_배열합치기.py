from collections import deque
n,m = map(int,input().split())

a_lst = list(map(int,input().split()))
b_lst = list(map(int,input().split()))
answer = []
a_now = 0
b_now = 0
a = a_lst[a_now]
b = b_lst[b_now]
while a_now < n or b_now < m:
    
    if a>=b:
        answer.append(b)
        b_now +=1
        if b_now == m:
            b = 10**10
        else:
            b = b_lst[b_now]
        
    else:
        answer.append(a)
        a_now +=1
        if a_now  ==  n:
            a = 10**10
        else:
            a = a_lst[a_now]
        
for i in answer:
    print(i,end = ' ')