# String
# Problem: 6550
# Memory: 29200KB
# Time: 88ms

A = ''
B = ''

while True:
    try:
        A, B = map(str, input().split())
    except:
        break

    flag = False
    cnt = 0
    target_cnt = len(A)
    for i in B:
        if i == A[cnt]:
            if cnt+1 == target_cnt:
                flag = True
                break
            cnt+=1
    if flag == True:
        print("Yes")
    else:
        print("No")
