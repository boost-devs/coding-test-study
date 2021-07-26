n = int(input())


max_num = 0
min_num = 10**10
lst = []
for _ in range(n):
    a,b = map(int,input().split())
    if min(a,b) < min_num:
        min_num = min(a,b)
    if max(a,b) > max_num:
        max_num = max(a,b)
    lst.append([a,b])
days = [0] * (max_num+1)
for work in lst:
    a,b = work
    for i in range(a,b+1):
        days[i] +=1
now_max = 0
start = min_num
cnt = 0
answer = 0
for i in range(min_num,max_num+1):
    if days[i] != 0:
        cnt +=1
        now_max = max(now_max, days[i])
    if days[i] ==0:
        answer += cnt * now_max
        cnt = 0
        now_max = 0

answer += cnt * now_max
print(answer)