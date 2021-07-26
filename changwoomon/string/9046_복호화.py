###### 9046번: 복호화
# https://www.acmicpc.net/problem/9046
# 메모리/시간: 31864KB / 96ms

import sys
from collections import Counter

input = sys.stdin.readline

T = int(input())
test_case = [list(map(str, input().rstrip())) for _ in range(T)]

for i in range(T):
    tmp = Counter(test_case[i])
    tmp -= Counter({" ": tmp[" "]})
    cnt = 0
    answer = ""
    for k, v in tmp.items():
        if v == max(tmp.values()):
            cnt += 1
            answer = k
    if cnt == 1:
        print(answer)
    else:
        print("?")