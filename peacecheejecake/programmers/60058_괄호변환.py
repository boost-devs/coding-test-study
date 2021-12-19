def solution(p): # 
    b = p.replace('(', '1').replace(')', '0')
    return convert(b).replace('1', '(').replace('0', ')')
        

def convert(b): # 메인 함수
    if not b:
        return ''
    
    u = find_u(b)
    v = b[len(u):]
    
    if is_right(u):
        nb = u + convert(v)
    else:
        nb = '1' + convert(v) + '0' + reverse(u[1:-1])
    return nb


def is_right(b): # `올바른 괄호 문자열`인지 검사한다.
    stack = []
    for d in b:
        if stack and stack[-1] != d:
            stack.pop()
        else:
            if not stack and d == '0':
                return False
            stack.append(d)
    return not stack


def find_u(b): # 최소 길이의 `균형잡힌 괄호 문자열`을 찾는다.
    count = 0
    nb = ''
    for d in b:
        count += (-1) ** int(d)
        nb += d
        if count == 0:
            break
    return nb


def reverse(b): # 이진수로 나타낸 괄호를 뒤집는다.
    if not b:
        return ''
    return f"{int('1' * len(b), 2) ^ int(b, 2):0{len(b)}b}"
