###### 15787번: 기차가 어둠을 헤치고 은하수를
# https://www.acmicpc.net/problem/15787
# 메모리/시간: 54312KB / 484ms

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

train = [[0] * 22 for _ in range(N+1)]

def func_1(train, ix):
    i, x = ix
    train[i][x] = 1
    return train

def func_2(train, ix):
    i, x = ix
    train[i][x] = 0
    return train

def func_3(train, i):
    i = i[0]
    for j in range(20, 0, -1):
        train[i][j] = train[i][j-1]
    return train

def func_4(train, i):
    i = i[0]
    for j in range(1, 21):
        train[i][j] = train[i][j+1]
    return train

func = [None, func_1, func_2, func_3, func_4]

for _ in range(M):
    _input = list(map(int, input().split()))
    f, args = _input[0], _input[1:]
    train = func[f](train, args)

check = set()
cnt = 0

for t in train[1:]:
    tmp = tuple(t[1:21])
    if tmp not in check:
        check.add(tmp)
        cnt += 1

print(cnt)
