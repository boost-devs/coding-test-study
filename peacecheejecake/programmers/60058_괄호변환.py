def solution(p):
    b = p.replace('(', '1').replace(')', '0')
    return convert(b).replace('1', '(').replace('0', ')')
        

def convert(b):
    if not b:
        return ''
    
    u = find_u(b)
    v = b[len(u):]
    
    if is_right(u):
        nb = u + convert(v)
    else:
        nb = '1' + convert(v) + '0' + reverse(u[1:-1])
    return nb


def is_right(b):
    stack = []
    for d in b:
        if stack and stack[-1] != d:
            stack.pop()
        else:
            if not stack and d == '0':
                return False
            stack.append(d)
    return not stack


def find_u(b):
    count = 0
    nb = ''
    for d in b:
        count += (-1) ** int(d)
        nb += d
        if count == 0:
            break
    return nb


def reverse(b):
    if not b:
        return ''
    return f"{int('1' * len(b), 2) ^ int(b, 2):0{len(b)}b}"
