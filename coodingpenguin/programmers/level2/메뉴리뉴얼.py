from itertools import combinations
from collections import Counter


def most_commons(counter):
    counter = counter.most_common()
    if not counter:
        return []
    max_count = counter[0][1]  # 최대 카운트
    menus = []  # 가장 많이 주문한 조합
    for comb, count in counter:
        if count == max_count and count > 1:
            menus.append("".join(comb))
        else:
            break
    return menus


def solution(orders, course):
    menus = []  # 코스요리 메뉴 구성
    for count in course:
        combs = []  # count 크기로 만들 수 있는 모든 조합
        for order in orders:
            combs += combinations(sorted(order), count)
        menus += most_commons(Counter(combs))  # 가장 많이 주문한 조합
    return sorted(menus)


if __name__ == "__main__":
    orders = ["XYZ", "XWY", "WXA"]
    course = [2, 3, 4]

    print(solution(orders, course))
