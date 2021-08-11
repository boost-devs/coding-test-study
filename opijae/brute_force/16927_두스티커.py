import sys
input = sys.stdin.readline

h,w = map(int, input().split())
n= int(input())
stikers = []
for _ in range(n):
    stikers.append(list(map(int,input().split())))
_max = 0
for i in range(n):
    h1,w1 =stikers[i] # 첫 스트커의 h,w
    for j in range(i+1,n):
        h2,w2 =stikers[j] # 두번째 스티커의 h,w
        # h1 h2 끼리 붙이는 경우
        if h1+h2<= h and  max(w1,w2)<= w:
            _max = max(_max,h1*w1 + w2*h2)
        elif h1+h2<= w and  max(w1,w2)<= h:
            _max = max(_max,h1*w1 + w2*h2)
        # w1 w2 끼리 붙이는 경우
        elif w1+w2<= w and  max(h1,h2)<= h:
            _max = max(_max,h1*w1 + w2*h2)
        elif w1+w2<= h and  max(h1,h2)<= w:
            _max = max(_max,h1*w1 + w2*h2)
        # h1 w2 끼리 붙이는 경우
        elif h1+w2<= h and  max(w1,h2)<= w:
            _max = max(_max,h1*w1 + w2*h2)
        elif h1+w2<= w and  max(w1,h2)<= h:
            _max = max(_max,h1*w1 + w2*h2)
        # w1 h2 끼리 붙이는 경우
        elif w1+h2<= w and  max(h1,w2)<= h:
            _max = max(_max,h1*w1 + w2*h2)
        elif w1+h2<= h and  max(h1,w2)<= w:
            _max = max(_max,h1*w1 + w2*h2)
print(_max)