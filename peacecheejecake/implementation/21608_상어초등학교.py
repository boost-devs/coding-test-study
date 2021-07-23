# https://www.acmicpc.net/problem/21608
# 상어 초등학교
# 33076 KB / 832 ms


from collections import defaultdict


n = int(input())

all_indices = [(r, c) for r in range(n) for c in range(n)]
adj_dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

classroom = [[0] * n for _ in range(n)]
in_seat = {}
friends = {}
for _ in range(n ** 2):
    s, f1, f2, f3, f4 = map(int, input().split())
    friends[s] = (f1, f2, f3, f4)
    
    # (조건 1) 좋아하는 학생 근처에서 주변 좋아하는 학생 수 세기
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
        tr, tc = cands_1[0] ## 유일하면 확정
    else: 
        # (조건 2) 빈 자리에서 주변 빈 자리 개수 세기
        empty = {}
        ## 조건 1의 후보들만(최댓값이 0일 때는 모든 자리) 검토
        gen_rc = cands_1 if cands_1 else all_indices
        for r, c in gen_rc:
            if (r, c) not in in_seat.values():
                empty[(r, c)] = 0
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
sat = 0
for r, c in all_indices:
    s = classroom[r][c]
    num_f = 0
    for dr, dc in adj_dirs:
        nr, nc = r + dr, c + dc
        if (
            nr >= 0 and nr < n and 
            nc >= 0 and nc < n and
            classroom[nr][nc] in friends[s]
        ):
            num_f += 1

    if num_f > 0:
        sat += 10 ** (num_f - 1)

print(sat)
