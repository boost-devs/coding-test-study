def step(elms, op_tgt):
    if len(elms) == 0:
        return elms

    temp = []
    left = elms[0]
    for i, op in enumerate(elms[1::2], 1):
        right = elms[2 * i]
        if op == op_tgt:
            left = str(eval(f"{left}{op}{right}"))
        else:
            temp.extend([left, op])
            left = right
    else:
        temp.append(left)
    return temp


def solution(expression):
    elms, op_set = [], set()
    digit = expression[0]
    for c in expression[1:]:
        if c.isdigit():
            digit += c
        else:
            op_set.add(c)
            elms.extend([digit, c])
            digit = ''
    else:
        elms.append(digit)
    
    max_prize = 0
    for first in op_set:
        first_result = step(elms, first)
        if len(op_set) < 3:
            prize = abs(eval(''.join(first_result)))
            max_prize = max(max_prize, prize)
        else:
            for second in op_set - {first}:
                second_result = step(first_result, second)
                prize = abs(eval(''.join(second_result)))
                max_prize = max(max_prize, prize)
    return max_prize
