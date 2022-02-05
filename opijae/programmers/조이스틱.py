def get_alpha(target):
    if ord(target) - 65 > 13:
        return 90 - ord(target)
    return ord(target) - 65

def solution(name):
    answer = 0
    for ch in name:
        answer += get_alpha(ch)
    n = len(name)
    move = n - 1
    for idx in range(n):
        next_idx = idx + 1
        while (next_idx < n) and (name[next_idx] == 'A'):
            next_idx += 1
        # idx 지금 까지 온 거리
        # n - next_idx = 앞으로 가야할 거리
        # 지금까지 간 거리랑 앞으로 갈 거리 비교 (뒤로 갈지 앞으로 갈지를 더함)
        distance = min(idx, n - next_idx)
        # 현재까지 온 길이(idx) + 앞으로 가야할 거리(n- next_idx) + 뒤로 갈지 앞으로 갈지를 더함
        # 매 지점마다 뒤로갈지 앞으로 갈지 정하면서 최소 값을 비교
        move = min(move, idx + n - next_idx + distance)

    answer += move
    return answer