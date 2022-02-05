from collections import deque


def solution(priorities, location):
    q = deque([
        (p, i == location) for i, p in enumerate(priorities)
    ])
    cnt = 0
    while q:
        head, is_mine = q.popleft()
        if q and max(t[0] for t in q) > head:
            q.append((head, is_mine))
        else:
            cnt += 1
            if is_mine:
                return cnt
