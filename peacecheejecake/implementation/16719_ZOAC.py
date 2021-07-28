# https://www.acmicpc.net/problem/16719
# ZOAC
# 33104 KB / 152 ms


from string import ascii_uppercase


def search(s, bag, start=0):
    if not s:
        return

    for pivot_char in ascii_uppercase:
        if pivot_char in s:
            pivot_idx = s.index(pivot_char)
            break
    
    bag.append((pivot_char, pivot_idx + start))
    search(s[pivot_idx + 1:], bag, start=start + pivot_idx + 1)
    search(s[:pivot_idx], bag, start=start)


s = input()

bag = []
search(s, bag)

seq = [""] * len(s)
for char, idx in bag:
    seq[idx] = char
    print("".join(seq))
