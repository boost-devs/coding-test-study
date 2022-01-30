from collections import defaultdict


def solution(s):
    len2set = defaultdict(set)
    digit = ''
    for c in s[1:-1]:
        if c == '{':
            elms = set()
        elif c == '}':
            elms.add(int(digit))
            digit = ''
            len2set[len(elms)] = elms
        elif c.isdigit():
            digit += c
        elif c == ',' and digit:
            elms.add(int(digit))
            digit = ''
    
    if len(len2set) == 1: # n이 1이면 유일한 원소만 포함
        return list(len2set[1])
    
    return [
        (len2set[l + 1] - len2set[l]).pop() 
        for l in range(0, max(len2set))
    ]
