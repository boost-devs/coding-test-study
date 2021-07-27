h,w = map(int,input().split())
lst = list(map(int,input().split()))

answer1 = [0] * len(lst)
answer2 = [0] * len(lst)
answer = 0

# 왼쪽에서 보기

now_h = 0
for i in range(len(lst)):
    if now_h < lst[i]:
        now_h = lst[i]
        continue
    answer1[i] = now_h - lst[i]


#오른쪽에서 보기

lst.reverse()
now_h = 0
for i in range(len(lst)):
    if now_h < lst[i]:
        now_h = lst[i]
        continue
    answer2[i] = now_h - lst[i]
answer2.reverse()

# 양방향 중 적은 양의 비를 채택함

for i in range(len(answer1)):
    answer += min(answer1[i],answer2[i])
print(answer)