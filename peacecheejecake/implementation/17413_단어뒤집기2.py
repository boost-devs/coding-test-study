# https://www.acmicpc.net/problem/17413
# 단어 뒤집기 2
# 29200 KB / 100 ms


s = input()

inverted = ''
ss = ''
in_tag = False
for c in s:
    if c == '<':
        inverted += ss[::-1]
        ss = '<'
        in_tag = True
    elif c == '>':
        inverted += ss + '>'
        ss = ''
        in_tag = False
    elif c == ' ' and not in_tag:
        inverted += ss[::-1] + ' '
        ss = ''
    else:
        ss += c
inverted += ss[::-1]

print(inverted)
