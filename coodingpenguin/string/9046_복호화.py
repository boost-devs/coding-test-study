# 문제: [BOJ 9046] 복호화
# 유형: 문자열, Counter
# 메모리/시간: 31824kb / 100ms

import sys
from collections import Counter

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    encoded = input().rstrip().replace(" ", "")
    if len(set(encoded)) == 1:
        print(encoded[-1])
    else:
        counter = Counter(encoded).most_common()
        if counter[0][1] == counter[1][1]:
            print("?")
        else:
            print(counter[0][0])
