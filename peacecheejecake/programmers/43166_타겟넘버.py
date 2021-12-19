def solution(numbers, target):
    l = len(numbers)
    answer = 0
    for i in range(1 << l):
        signs = f"{i:0{l}b}" # 0이면 +, 1이면 -
        case = sum((-1) ** int(t) * num for t, num in zip(signs, numbers))
        answer += int(case == target)
    return answer
