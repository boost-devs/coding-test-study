# 문제: [BOJ 21921] 블로그
# 유형: 슬라이딩 윈도우
# 메모리/시간: 58192kb / 184ms
# 참고: https://welog.tistory.com/317

import sys

input = sys.stdin.readline


def get_max_visitors(size, visitors):
    # 윈도우 크기가 1이라면
    if size == 1:
        max_visitors = max(visitors)
        # 최댓값과 그 개수를 반환한다
        return max_visitors, visitors.count(max_visitors)
    # 총 방문자수가 0이라면
    if not sum(visitors):
        # SAD를 반환한다
        return None, "SAD"
    window = sum(visitors[:size])  # 윈도우
    max_visitors = window  # 최대 방문수
    count = 1  # 최대 방문수일 때의 횟수

    for i in range(size, len(visitors)):
        window += visitors[i]  # 새로운 요소 추가
        window -= visitors[i - size]  # 기존 요소 제거
        # 최고 방문수보다 많다면
        if window > max_visitors:
            max_visitors = window  # 갱신
            count = 1  # 카운트 1로 초기화
        # 최고 방문수와 같다면
        elif window == max_visitors:
            count += 1  # 카운트 증가

    return max_visitors, count


N, X = map(int, input().split())  # 지난 일수, 기간
visitors = list(map(int, input().split()))  # 방문수 기록
max_visitors, count = get_max_visitors(X, visitors)

if not max_visitors:
    print(count)
else:
    print(max_visitors)
    print(count)
