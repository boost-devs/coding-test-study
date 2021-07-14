from collections import defaultdict

n = int(input())
watch = defaultdict(list)

for _ in range(n):
    a,b = map(int,input().split())
    watch[a].append(b)

answer = 0
for key in watch:
    if len(set(watch[key])) ==1:
        continue
    now = watch[key][0]
    cnt = 0
    for i in range(1,len(watch[key])):
        if now != watch[key][i]:
            cnt+=1
            now = watch[key][i]
    answer += cnt
print(answer)