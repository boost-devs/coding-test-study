# u,v 분리 이때 u는 균형잡힌 괄호
def split(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        # ( 와 ) 의 수가 같으면 return
        if cnt == 0:
            return p[: i + 1], p[i + 1 :]

#  u가 올바른 괄호인지 확인
def isRight(u):
    stack = []
    # 시작이 )면 false
    if u[0] ==')':
        return False
    # stack으로 올바른 괄호가 맞는지 확인
    for c in u:
        if stack and stack[-1] != c:
            stack.pop()
        else:
            stack.append(c)
    # stack이 비어있으면 True
    if stack:
        return False
    else:
        return True

# 문자열 뒤집음
def convt(u):
    temp = ''
    for c in u:
        if c =='(':
            temp += ')'
        else:
            temp += '('
    return temp

# 문제 설명대로 구현
def dfs(p):
    if len(p) == 0:
        return ''
    u,v = split(p)
    if isRight(u):
        return u + dfs(v)
    else:
        return '(' + dfs(v) + ')' + convt(u[1:-1])


def solution(p):
    return dfs(p)