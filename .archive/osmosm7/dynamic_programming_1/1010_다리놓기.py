##### 1010_다리놓기

n = int(input())
test = []
for _ in range(n):
    max_num = 0
    
    a,b = map(int,input().split())
    test.append([a,b])
    if b > max_num:
        max_num = b
lst = [1] * (max_num+1)
for i in range(2, b+1):
    lst[i] = i * lst[i-1]

for idx in range(n):
    a,b = test[idx]
    print(int(lst[b]/(lst[a] * lst[b-a])))