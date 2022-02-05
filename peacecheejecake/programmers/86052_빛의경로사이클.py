def solution(grid):
    n = len(grid)
    visited = [[[False] * 4 for _ in range(n)] for _ in range(n)]

    # def search_cycle(si, sj):
    #     for dir_idx in range(4):
