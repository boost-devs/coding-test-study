n = int(input())
light = list(map(int,input().split()))
m = int(input())

for i in range(m):
    s, num = map(int,input().split())

    if s == 1:
        for j in range(1,len(light)+1):
            now = (j * num)-1
            if  now < len(light):
                light[now] = 1-light[now]
    if s == 2:
        idx = num-1
        light[idx] = 1 - light[idx]
        lt,rt = idx-1,idx+1
        while True:
            if lt not in range(len(light)) or rt not in range(len(light)):
                break
            
            if light[lt] != light[rt]:
                break
            light[lt] = 1-light[lt]
            light[rt] = 1-light[rt]
            lt -=1
            rt +=1
cnt = 0
for i in light:
    print(i, end = ' ')
    cnt +=1
    if cnt == 20:
        print('')
        cnt = 0