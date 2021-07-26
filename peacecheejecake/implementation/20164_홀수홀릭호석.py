# https://www.acmicpc.net/problem/20164
# 홀수 홀릭 호석
# 29200 KB / 72 ms


def count_odd(num):
    count = 0
    for d in num:
        if int(d) % 2 == 1:
            count += 1
    return count


def simulate(num):
    if len(num) == 1:
        return (count_odd(num),) * 2

    num_odds = count_odd(num)
    if len(num) == 2:
        num_ = str(sum(map(int, num)))
        min_, max_ = simulate(num_)
    else:
        min_, max_ = 33, 0
        for i in range(1, len(num) - 1):
            for j in range(i + 1, len(num)):
                num_ = str(sum(map(int, (num[:i], num[i:j], num[j:]))))
                _min, _max = simulate(num_)
                
                min_ = min(min_, _min)
                max_ = max(max_, _max)
    return min_ + num_odds, max_ + num_odds


n = input()
print(' '.join(map(str, simulate(n))))
