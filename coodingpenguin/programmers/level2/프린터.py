from collections import deque


def is_highest(threshold, queue):
    for p, _ in queue:
        if p > threshold:
            return False
    return True


def solution(priorities, location):
    queue = deque([(p, n) for n, p in enumerate(priorities)])
    count = 1   # 프린트 순서
    while queue:
        # 인쇄 목록의 가장 앞에 있는 문서를 꺼낸다
        p, n = queue.popleft()
        # 뒤에 중요도가 높은 문서가 존재한다면
        if not is_highest(p, queue):
            queue.append((p, n))    # 대기목록 가장 마지막으로 넣는다
            continue
        # 아니라면
        if n == location:
            # 요청한 인쇄라면 순서를 반환한다
            return count
        count += 1  # 문서를 인쇄한다