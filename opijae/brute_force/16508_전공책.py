import sys
from itertools import combinations
input = sys.stdin.readline

target = input().rstrip()
n = int(input())

price = []
book = []
arr = []
for _ in range(n):
    p,b =input().split()
    arr.append([int(p),b])
combi = []
for i in range(1,n+1): # nC1 .....nCn 까지 조합을 만듬
    combi.extend(list(combinations(arr,i))) 
_min = 1000000000
for comb in combi: # 매 조합마다
    temp =''
    _price = 0
    for c in comb:
        temp += c[1]  # 모든 문자열을 연결한다.
        _price += c[0]
    flag = True  # temp 문자열이 target문자열 단어들을 포함하는지 확인용
    for s in target:
        if s in temp:
            temp = temp.replace(s,'a',1)
        else:
            flag = False
            break 
    if flag: # 확인이 되면 값 업데이트
        _min = min(_min,_price)
if _min == 1000000000:
    print(-1)
else:
    print(_min)