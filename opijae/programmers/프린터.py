from collections import deque
def solution(priorities, location):
    priorities = deque(priorities)
    # 기존의 우선순위에 index 저장
    for i, priority in enumerate(priorities):
        priorities[i] = [priority,i]
    cnt = 0
    while(priorities):
        # 최고 우선순위 찾기
        _max = max(priorities, key = lambda x: x[0])[0]
        # q의 첫번째 값의 우선순위가 최고 우선순위인지 확인
        if priorities[0][0]<_max:
            priorities.append(priorities.popleft())
        else:
            cnt += 1
            _, seq = priorities.popleft()
            if seq == location:
                return cnt