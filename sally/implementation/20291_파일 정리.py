# Implementation
# Problem: 20291
# Memory: 42440KB
# Time: 2312ms

mylist = {}
N = int(input())
for i in range(N):
    ext = input().split('.')[1]
    if ext in mylist:
        mylist[ext] += 1
    else:
        mylist[ext] = 1

mylist = sorted(mylist.items())
for k, v in mylist:
    print(k + ' ' + str(v))