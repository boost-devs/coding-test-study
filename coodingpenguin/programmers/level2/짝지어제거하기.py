def compress(s):
    stack = [s[0]]
    for i in range(1, len(s)):
        if stack and s[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(s[i])
    return stack


def solution(s):
    # 압축이 되면
    if compress(s):
        return 0  # 0을 반환
    return 1  # 안 되면 1을 반환
