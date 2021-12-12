dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def solution(rows, columns, queries):
    matrix = [[j * columns + i for i in range(1, columns + 1)] for j in range(rows)]
    result = []
    for y1, x1, y2, x2 in queries:
        min_num = 10000  # 최소 숫자
        cy, cx, cd = y1 - 1, x1 - 1, 0  # 현재 위치(y, x)와 이동 방향
        new_matrix = [row[:] for row in matrix]
        # 모든 방향을 돌 때까지 반복
        while cd < 4:
            min_num = min(min_num, matrix[cy][cx])  # 최솟값 갱신
            ny, nx = cy + dirs[cd][0], cx + dirs[cd][1]  # 이동할 위치
            # 범위에서 벗어나면
            if (ny < y1 - 1 or ny > y2 - 1) or (nx < x1 - 1 or nx > x2 - 1):
                cd += 1  # 방향을 바꾼다
                continue
            new_matrix[ny][nx] = matrix[cy][cx]
            cy, cx = ny, nx
        matrix = new_matrix
        result.append(min_num)
    return result
