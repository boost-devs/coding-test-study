from collections import defaultdict, deque
n = int(input())
lst_dict = defaultdict(list)
for _ in range(n-1):
    a,b = map(int,input().split(' '))
    lst_dict[a].append(b)
    lst_dict[b].append(a)


next = deque([1])
done = []
while len(next)>0:
    for _ in range(len(next)):
        now = next.popleft()
        for i in lst_dict[now]:
            next.append(i)
            done.append([now,i])
            lst_dict[i].remove(now)
            
# 2부터 부모 노드 출력
now = 2
done.sort(key = lambda x: x[1])
for dir in done:
    if dir[1] == now:
        print(dir[0])
        now+=1
        if now == n+1:
            break