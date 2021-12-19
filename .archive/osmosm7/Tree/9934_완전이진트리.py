from collections import deque

n = int(input())
lst = list(map(int,input().split(' ')))

step = 0
next_lst = deque([lst])
now_lst = deque()
while True:
    now_lst = next_lst
    next_lst = deque([])
    for i in range(len(now_lst)):
        now = now_lst.popleft()
        now_len = len(now)
        print(now[now_len//2],end = ' ')
        next_lst.append(now[:(now_len//2)])
        next_lst.append(now[(now_len//2+1):])
    step += 1
    if step ==n:
        break
    print('')