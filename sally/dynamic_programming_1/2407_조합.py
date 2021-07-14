# DP
# Problem: 2407
# Memory: 31312KB
# Time: 72ms

import math

N, M = input().split()
N = int(N)
M = int(M)

result = math.factorial(N)//math.factorial(N-M)//math.factorial(M)

print(result)