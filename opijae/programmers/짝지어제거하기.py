def solution(s):
    stack=[]
    for c in s:
        # stack의 마지막이랑 현재 문자가 같으면 제거
        if stack and c ==stack[-1]:
            stack.pop()
        else:
            stack.append(c)
    if len(stack)==0:
        return 1
    else:
        return 0