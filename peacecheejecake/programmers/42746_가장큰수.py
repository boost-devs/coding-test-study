def solution(numbers):
    if not any(x > 0 for x in numbers):
        return "0"

    def key(x):
        l, x = len(x), x.ljust(4, x[0])
        if x[1] >= x[0]:
            l = -l
        return (x, l)

    return ''.join(sorted(map(str, numbers), key=key, reverse=True))
