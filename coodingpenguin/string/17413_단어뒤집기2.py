import sys
import re

input = sys.stdin.readline


def find_brkt_pos(s):
    pos = []
    for idx, letter in enumerate(s):
        if letter in "<>":
            pos.append(idx)
    return pos


def reverse_word(s):
    return " ".join([w[::-1] for w in s.split()])


def convert_string(s):
    brkt = find_brkt_pos(s)
    result = ""

    if not brkt:
        return reverse_word(s)

    if brkt[0] > 0:
        result += reverse_word(s[: brkt[0]])
    for i in range(len(brkt) - 1):
        if not i % 2:
            result += s[brkt[i] : brkt[i + 1] + 1]
        else:
            result += reverse_word(s[brkt[i] + 1 : brkt[i + 1]])
    if brkt[-1] < len(s):
        result += reverse_word(s[brkt[-1] + 1 :])
    return result


s = input().rstrip()
print(convert_string(s))
