OPEN, CLOSE = "(", ")"


def split(p):
    count = {OPEN: 0, CLOSE: 0}
    for i in range(len(p)):
        count[p[i]] += 1
        if count[OPEN] == count[CLOSE]:
            return p[: i + 1], p[i + 1 :]


def check(p_list):
    stack = []
    while p_list:
        item = p_list.pop(0)
        if stack and (item == CLOSE and stack[-1] == OPEN):
            stack.pop()
        else:
            stack.append(item)
    if stack:
        return False
    return True


def reverse(p):
    return "".join([CLOSE if i == OPEN else OPEN for i in p])


def solution(p):
    # 빈 문자열인 경우
    if not p:
        return p  # 바로 반환
    u, v = split(p)  # 균형잡힌 괄호 문자열 2개로 분리
    if check(list(u)):
        return u + solution(v)  # u가 올바른 괄호 문자열인 경우
    return OPEN + solution(v) + CLOSE + reverse(u[1:-1])  # u가 올바른 괄호 문자열이 아닌 경우


if __name__ == "__main__":
    p = "()))((()"
    print(solution(p))
