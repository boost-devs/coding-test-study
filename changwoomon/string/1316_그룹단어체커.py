###### 1316번: 그룹 단어 체커
# https://www.acmicpc.net/problem/1316
# 메모리/시간: 31864KB / 96ms

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

cnt = 0
for _ in range(N):
    _input = deque([x for x in input().rstrip()])
    str_len = len(_input)
    ck = set()
    tmp = ""
    while _input:
        x = _input.popleft()
        if x not in ck:
            ck.add(x)
            tmp = x
            str_len -= 1
        else:
            if x == tmp:
                str_len -= 1
            else:
                break
    if str_len == 0:
        cnt += 1

print(cnt)