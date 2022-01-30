from itertools import permutations


def generate_prime_nums(nums):
    max_num = int("".join(sorted(nums, reverse=True)))
    prime_nums = set(range(2, max_num + 1))
    for i in range(2, max_num + 1):
        if i in prime_nums:
            prime_nums -= set(range(2 * i, max_num + 1, i))
    return prime_nums


def solution(numbers):
    prime_nums = generate_prime_nums(numbers)
    result = set()
    for r in range(1, 8):
        combs = permutations(numbers, r)
        for comb in combs:
            num = int("".join(comb))
            if num in prime_nums:
                result.add(num)
    return len(result)
