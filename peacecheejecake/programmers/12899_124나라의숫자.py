def solution(n):
    nn = n
    num_digit = 0
    while nn > 0:
        num_digit += 1
        nn -= 3 ** num_digit
            
    n -= (3 ** num_digit - 3) // 2 + 1
    ternary = ''
    while n > 0:
        n, r = divmod(n, 3)
        ternary = str(r) + ternary
    return (
        ternary
        .rjust(num_digit, '0')
        .replace('2', '4')
        .replace('1', '2')
        .replace('0', '1')
    )
    