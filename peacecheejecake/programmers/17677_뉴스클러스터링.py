import re
from collections import Counter


def count_pairs(s):
    pairs = re.findall(r'(?=([a-z]{2}))', s.lower())
    return Counter(pairs)


def solution(*strs):
    set1, set2 = map(count_pairs, strs)
    num_inter, num_union = 0, 0
    for pair in set(set1) | set(set2):
        count1 = set1.get(pair, 0)
        count2 = set2.get(pair, 0)
        num_inter += min(count1, count2)
        num_union += max(count1, count2)
    score = num_inter / num_union if num_union > 0 else 1
    return int(score * 65536)
