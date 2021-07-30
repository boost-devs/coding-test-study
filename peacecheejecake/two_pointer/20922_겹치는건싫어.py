# https://www.acmicpc.net/problem/20922
# 겹치는 건 싫어
# 54960 KB / 468 ms


from collections import Counter, defaultdict


N, K = map(int, input().split())
arr = [int(a) for a in input().split()]
        
p_counter = Counter(arr[:K])

excess = set()
max_len = K
i, j = 0, K
while j < N:
    head, to_add = arr[i], arr[j]

    p_counter[to_add] = p_counter.get(to_add, 0) + 1
    j += 1

    if p_counter[to_add] > K or excess:
        p_counter[head] -= 1
        i += 1

        if p_counter[head] == K and head in excess:
            excess.remove(head)
        if p_counter[to_add] == K + 1 and to_add != head:
            excess.add(to_add)
    else:
        max_len += 1

print(max_len)
