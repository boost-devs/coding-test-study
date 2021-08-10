# https://www.acmicpc.net/problem/16439
# 31312 KB / 256 ms


from itertools import permutations


N, M = map(int, input().split())
chicken_matrix = []
for _ in range(N):
    chicken_matrix.append([int(p) for p in input().split()])

max_pref_sum = 0
for c1, c2, c3 in permutations(range(M), 3):
    pref_sum = 0
    for prefs in chicken_matrix:
        pref = max(prefs[c1], prefs[c2], prefs[c3])
        pref_sum += pref
    max_pref_sum = max(max_pref_sum, pref_sum)

print(max_pref_sum)
