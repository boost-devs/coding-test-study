import sys
from itertools import product
input = sys.stdin.readline

n = int(input())
arr=[]
for _ in range(n):
    arr.append(list(map(int, input().split())))

prods = product([0,1],repeat=n) # 0 과 1로 조합해 재료를 쓸지 안쓸지 결정한다.
_min = 100000000000000000
next(iter(prods)) # 첫번째 값(모두 0으로 이루어진 경우는 뺀다)
for prod in prods:
    temp = 1
    temp1 = 0
    for i in range(n):
        if prod[i]: # 재료를 사용한다면
            temp *= arr[i][0]
            temp1 += arr[i][1]
    _min = min(_min, abs(temp-temp1))
print(_min)