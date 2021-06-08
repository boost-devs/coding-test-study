# 문제: [BOJ 1764] 듣보잡
# 유형: 집합
# 메모리/시간: 41876kb / 116ms

import sys

input = sys.stdin.readline

# 입력
n, m = map(int, input().split())  # 듣도 못한 사람 수, 보도 못한 사람 수
n_list = set([input().rstrip() for _ in range(n)])  # 듣도 못한 사람 리스트
m_list = set([input().rstrip() for _ in range(m)])  # 보도 못한 사람 리스트

# 교집합
nm_list = sorted(n_list & m_list)

# 출력
print(len(nm_list))  # 듣보잡 수
for name in nm_list:
    print(name)  # 듣보잡 이름
