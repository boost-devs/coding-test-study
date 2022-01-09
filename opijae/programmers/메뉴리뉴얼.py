from itertools import combinations 
from collections import Counter
def solution(orders, course):
    answer = []
    # 메뉴를 오름차순으로 정렬
    s_orders=[sorted(order) for order in orders]
    for c in course:
        temp_list = []
        # 코스메뉴 수 많큼 코스 조합짜기
        for order in s_orders:
            temp = combinations(order,c)
            temp_list.extend(list(temp)) # 나올 수 있는 조합
        max_b=0
        # 많이 나온 순대로 코스요리 채택
        for a,b in Counter(temp_list).most_common():
            if b<2:
                break
            if max_b<=b:
                max_b = b
                answer.append(''.join(a))
    return sorted(answer)