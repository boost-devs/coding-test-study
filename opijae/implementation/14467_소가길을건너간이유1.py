import sys
from collections import defaultdict
input = sys.stdin.readline
n=int(input())
cow = [-1]*(n+1) # 소 배열
answer = 0 
for _ in range(n): 
    a, b = map(int, input().split())
    if cow[a] == -1: # 소가 처음 관측 되었을때
        cow[a] = b
    elif cow[a] != b: # 소가 길을 건넜으면 
        cow[a] = b
        answer +=1

print(answer)