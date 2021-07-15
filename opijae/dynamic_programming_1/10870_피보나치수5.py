import sys
input = sys.stdin.readline
n= int(input())
fib=[0,1]
if n<2:
    print(fib[n])
else:
    for i in range(n-1):
        fib.append(fib[i]+fib[i+1])
    print(fib[-1])