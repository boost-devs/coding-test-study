# https://www.acmicpc.net/problem/20436
# ZOAC 3
# 29200 KB / 80 ms


key_rows = [
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
    ['z', 'x', 'c', 'v', 'b', 'n', 'm'],
]
ends_of_left = [4, 4, 3]
keyboard = {}
for i, row in enumerate(key_rows):
    for j, key in enumerate(row):
        hand = 'l' if j <= ends_of_left[i] else 'r'
        keyboard[key] = (i, j, hand)

l, r = input().split()
duration = 0
for char in input():
    i, j, h = keyboard[char]
    if h == 'l':
        i_0, j_0, _ = keyboard[l]
        l = char
    else:
        i_0, j_0, _ = keyboard[r]
        r = char
    duration += abs(i - i_0) + abs(j - j_0) + 1

print(duration)
