def solution(s):
    length = len(s)
    min_compressed = length  # 최소 압축 문자열 길이
    for offset in range(1, length // 2 + 1):
        stack = []
        for base in range(0, length, offset):
            current = s[base : base + offset]
            if stack and current == stack[-1][0]:
                top = stack.pop()
                if current == top[0]:
                    stack.append((current, top[1] + 1))
                    continue
            stack.append((current, 1))
        compressed = 0  # 압축된 문자열 길이
        for word, count in stack:
            compressed += len(word) if count == 1 else len(word) + len(str(count))
        min_compressed = min(compressed, min_compressed)  # 최솟값 갱신
    return min_compressed
