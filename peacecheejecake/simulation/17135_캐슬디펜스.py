# https://www.acmicpc.net/problem/17135
# 32360 KB / 320 ms


from itertools import combinations
from collections import deque
from copy import deepcopy


N, M, D = map(int, input().split())
enemy_map = [[int(x) for x in input().split()] for _ in range(N)]

adj_dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
all_pos_combs = combinations(range(M), 3)
max_attacks = 0
for pos_comb in all_pos_combs:
    n = N
    _enemy_map = deepcopy(enemy_map)
    num_attacks = 0
    for _ in range(N):
        dead_enemy = set()
        for arch in pos_comb:
            # check if an enemy is 1 cell ahead
            if _enemy_map[n - 1][arch] == 1:
                dead_enemy.add((n - 1, arch))
                continue
            
            # bfs
            min_dist = D
            nearests = []
            visited = [[False] * M for _ in range(n)]
            visited[-1][arch] = True
            queue = deque([(n - 1, arch, 1)])
            while queue:
                r, c, d = queue.popleft()
                if d >= min_dist:
                    continue
                
                for dr, dc in adj_dirs:
                    rn, cn, dn = r + dr, c + dc, d + 1
                    if (rn < 0 or rn >= n or cn < 0 or cn >= M or 
                        visited[rn][cn]):
                        continue
                    
                    visited[rn][cn] = True
                    if _enemy_map[rn][cn] == 1:
                        nearests.append((rn, cn))
                        min_dist = dn
                    else:
                        queue.append((rn, cn, dn))
            
            # update leftmost
            if nearests:
                to_attack = min(nearests, key=lambda x: x[1])
                dead_enemy.add(to_attack)

        # count attacks & kill attacked
        num_attacks += len(dead_enemy)
        for ra, ca in dead_enemy:
            _enemy_map[ra][ca] = 0
        
        # move enemies
        _enemy_map = _enemy_map[:-1]
        n -= 1
        
    max_attacks = max(max_attacks, num_attacks)

print(max_attacks)
