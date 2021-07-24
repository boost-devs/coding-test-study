# https://www.acmicpc.net/problem/15787
# 기차가 어둠을 헤치고 은하수를
# 30224 KB / 220 ms


import sys

def input():
    return sys.stdin.readline().rstrip()


n, m = map(int, input().split())

train = [0] * n
for _ in range(m):
    line = [int(arg) - 1 for arg in input().split()]
    if len(line) == 3:
        op, i, x = line
    else:
        op, i = line

    if op == 0:
        train[i] |= (1 << x)
    elif op == 1:
        train[i] -= (train[i] & (1 << x))
    elif op == 2:
        train[i] <<= 1
        train[i] -= (train[i] & (1 << 20)) # 20번째 자리에 승객이 있으면 하차
    else:
        train[i] >>= 1
    
print(len(set(train)))
