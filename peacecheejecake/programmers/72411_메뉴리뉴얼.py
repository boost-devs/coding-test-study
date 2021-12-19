from collections import defaultdict
from itertools import combinations


def solution(orders, course):
    counter = {num: defaultdict(int) for num in course}
    for order in orders:
        for num in course:
            if num > len(order):
                break
            for comb in combinations(sorted(order), num):
                counter[num][''.join(comb)] += 1
                
    cands = []
    for count_dict in counter.values():
        if count_dict:
            max_count = max(count_dict.values())
            if max_count >= 2:
                cands.extend(k for k, v in count_dict.items() if v == max_count)
    return sorted(cands)
