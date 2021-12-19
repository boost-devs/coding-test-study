###### 16926번: 배열 돌리기 1
# https://www.acmicpc.net/problem/16926
# 메모리/시간: 34508KB / 180ms

import sys
from collections import deque

input = sys.stdin.readline

N, M, R = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(N)]

def rotate(arr):
    global N, M, R
    queue = deque()
    width, height = M, N
    layer = min(width, height) // 2
    x, y = 0, 0
    
    while layer >= 1:
        for i in range(height-1):
            queue.append(arr[x+i][y])
        for i in range(width-1):
            queue.append(arr[x+height-1][y+i])
        for i in range(height-1):
            queue.append(arr[x+height-1-i][y+width-1])
        for i in range(width-1):
            queue.append(arr[x][y+width-1-i])

        queue.rotate(R)

        for i in range(height-1):
            arr[x+i][y] = queue.popleft()
        for i in range(width-1):
            arr[x+height-1][y+i] = queue.popleft()
        for i in range(height-1):
            arr[x+height-1-i][y+width-1] = queue.popleft()
        for i in range(width-1):
            arr[x][y+width-1-i] = queue.popleft()
        
        width -= 2
        height -= 2
        x += 1
        y += 1
        layer = min(width, height) // 2

    return arr

for row in rotate(array):
    print(*row)