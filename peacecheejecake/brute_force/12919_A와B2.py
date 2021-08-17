# https://www.acmicpc.net/problem/12919
#

def check(s, t, backward):
    if s[0] == 'B' and t[0] == 'A':
        return False

    s = s[::(-1) ** backward]
    start, end = 0, len(s)
    is_possible = False
    while end <= len(t):
        u = t[start:end]
        if (u == s and
            t[:start].count('B') == t[end:].count('B') + backward):
            is_possible = True
            break
        start += 1
        end += 1
    return is_possible


s = input()
t = input()

print(int(check(s, t, False) or check(s, t, True)))
