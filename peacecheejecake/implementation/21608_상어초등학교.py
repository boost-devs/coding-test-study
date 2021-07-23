# https://www.acmicpc.net/problem/21608
# 상어 초등학교
# 


from collections import defaultdict


n = int(input())
classroom = [[0] * n for _ in range(n)]
in_seat = {}
adj_dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
friends = {}
for _ in range(n ** 2):
    s, f1, f2, f3, f4 = map(int, input().split())
    friends[s] = (f1, f2, f3, f4)
    nearby = defaultdict(int)
    for f in (f1, f2, f3, f4):
        if in_seat.get(f) is not None:
            fr, fc = in_seat[f]
            for dr, dc in adj_dirs:
                nr, nc = fr + dr, fc + dc
                if (
                    nr >= 0 and nr < n and
                    nc >= 0 and nc < n and
                    (nr, nc) not in in_seat.values()
                ):
                    nearby[(nr, nc)] += 1
    
    max_num = max(nearby.values()) if nearby else 0
    cands_1 = [
        coord for coord, num in nearby.items()
        if num == max_num
    ]
    if len(cands_1) == 1:
        tr, tc = cands_1[0]
    else:
        empty = defaultdict(int)
        if len(cands_1) > 1:
            gen = cands_1
        else:
            gen = zip(range(n), range(n))
        
        for r, c in gen:
            for dr, dc in adj_dirs:
                nr, nc = r + dr, c + dc
                if (
                    nr >= 0 and nr < n and 
                    nc >= 0 and nc < n and
                    (nr, nc) not in in_seat.values()
                ):
                    empty[(r, c)] += 1
        
        max_num = max(empty.values())
        cands_2 = [
            coord for coord, num in empty.items()
            if num == max_num
        ]
        if len(cands_2) == 1:
            tr, tc = cands_2[0]
        else:
            tr, tc = sorted(cands_2)[0]

    # 자리에 앉기
    classroom[tr][tc] = s
    in_seat[s] = (tr, tc)

# 만족도 조사
sum_sat = 0
for r in range(n):
    for c in range(n):
        s = classroom[r][c]
        sat = 0
        for dr, dc in adj_dirs:
            nr, nc = r + dr, c + dc
            if (
                nr >= 0 and nr < n and 
                nc >= 0 and nc < n and
                classroom[nr][nc] in friends[s]
            ):
                sat += 1

        if sat >= 1:
            sum_sat += 10 ** (sat - 1)

print(sum_sat)
