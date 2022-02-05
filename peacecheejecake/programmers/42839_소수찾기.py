from itertools import permutations


def is_prime(num: str):
    num = int(num)
    if num == 2:
        return True
    elif num < 2 or num % 2 == 0:
        return False

    for q in range(3, int(num ** 0.5) + 1, 2):
        if num % q == 0:
            return False
    return True


def solution(numbers):
    primes = set()
    for r in range(1, len(numbers) + 1):
        for num_tup in permutations(numbers, r):
            num_str = ''.join(num_tup)
            if is_prime(num_str):
                primes.add(int(num_str))
    return len(primes)
