# 문제: [BOJ 1764] 듣보잡
# 유형: 집합
# 메모리/시간: 41876kb / 116ms

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
n_list = set([input().rstrip() for _ in range(n)])
m_list = set([input().rstrip() for _ in range(m)])

nm_list = sorted(n_list & m_list)

print(len(nm_list))
for name in nm_list:
    print(name)
