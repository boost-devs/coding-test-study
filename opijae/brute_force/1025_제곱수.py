import sys
input = sys.stdin.readline

n,m = map(int, input().split())

def is_square(n):
    if n & 0x0f in [0,1,4,9]:
        temp = n ** 0.5
        if int(temp) ** 2 == n:
            return True
        else:
            return False
    else:
        return False

arr = []
for _ in range(n):
    arr.append(list(map(int,input().strip())))

_max = -1
for i in range(n):
    for j in range(m): # 모든 경우 탐색
        for diff1 in range(-n,n): # 열 공차
            for diff2 in range(-m,m): # 행 공차
                if not diff1 and not diff2: # 0,0 이면 무한루프
                    continue
                step = 0
                x= i
                y= j
                value = ''
                while 0<=x<n and 0<=y<m:  # index 조건
                    value += str(arr[x][y])
                    step += 1
                    value_int = int(value)
                    if  is_square(value_int):
                        _max = max(_max,value_int)

                    x = i + step * diff1 # 다음 값 갱신
                    y = j + step * diff2
print(_max)
