# https://www.acmicpc.net/problem/21315
# 31568 KB / 88 ms


from math import log2


N = int(input())
after_shuffle = [int(x) for x in input().split()]

shuffle_maps = [None, [-1, -2] + list(range(N - 2))]
max_k = int(log2(N))
for k in range(2, max_k + 1):
    new_map = (
        shuffle_maps[k - 1][:2 ** (k - 1)] 
        + list(range(-2 ** k, -2 ** (k - 1)))
        + list(range(N - 2 ** k))
    )
    shuffle_maps.append(new_map)

for k1 in range(1, max_k + 1):
    for k2 in range(1, max_k + 1):
        cards = list(range(1, N + 1))
        cards = [cards[j] for j in shuffle_maps[k1]]
        cards = [cards[j] for j in shuffle_maps[k2]]
        if cards == after_shuffle:
            break
    else:
        continue
    break

print(k1, k2)
