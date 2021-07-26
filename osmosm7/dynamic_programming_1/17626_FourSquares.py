n = int(input())
lst = [4]* (n+1)
lst[1] = 1

for i in range(2,n+1):
    if int(i**(1/2)) **2 ==i:
        lst[i] =1
        continue
    for j in range(n):
        if j **2 > n:
            break
        lst[i] = min(lst[i],lst[i-j*j]+lst[j*j])
        if lst[i] ==2:
            break
print(lst[-1])
