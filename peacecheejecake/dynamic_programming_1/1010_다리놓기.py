# https://www.acmicpc.net/problem/1010
# 다리 놓기
# 31312 KB / 68 ms

import sys
import math

for _ in range(int(input())):
    n, m = map(int, sys.stdin.readline().strip().split())
    num_cases = (
        math.prod(range(m, m - n, -1)) // 
        math.prod(range(n, 0, -1))
    )
    
    print(num_cases)