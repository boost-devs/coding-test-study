digits = "124"


def solution(n):
    share, rest = divmod(n - 1, 3)  # 몫, 나머지
    if not share:
        return digits[rest]
    return solution(share) + digits[rest]
