# https://www.acmicpc.net/problem/20437
# 문자열 게임 2

from collections import defaultdict

T = int(input())

for _ in range(T):
    char_dict = defaultdict(list)
    for i, c in enumerate(input()):
        char_dict[c].append(i)
    k = int(input())
    cands = [idx for idx in char_dict.values() if len(idx) >= k]
    
    if not cands:
        print(-1)
    else:
        min_, max_ = 10000, 0
        for cand in cands:
            for i in range(len(cand) - k + 1):
                l = cand[i + k - 1] - cand[i] + 1
                min_ = min(min_, l)
                max_ = max(max_, l)

        print(f"{min_} {max_}")
