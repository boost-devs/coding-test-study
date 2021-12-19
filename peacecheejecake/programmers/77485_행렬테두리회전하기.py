def solution(rows, columns, queries):
    matrix = []
    for r in range(rows):
        matrix.append([r * columns + c + 1 for c in range(columns)])
    
    result = []
    for query in queries:
        rt, ct, rb, cb = (z - 1 for z in query) # 좌표를 0부터 시작하게 변경
        corners = [(rt, ct), (rt, cb), (rb, cb), (rb, ct)] # 네 모서리 좌표; 왼쪽 위부터 시계방향
        coords, elements = [], []
        for i, (ro, co) in enumerate(corners):
            rn, cn = corners[(i + 1) % 4]
            if rn == ro: # 좌/우
                for c in range(co, cn, (cn - co) // abs(cn - co)):
                    coords.append((ro, c))
                    elements.append(matrix[ro][c])
            elif cn == co: # 상/하
                for r in range(ro, rn, (rn - ro) // abs(rn - ro)):
                    coords.append((r, co))
                    elements.append(matrix[r][co])
        
        result.append(min(elements)) # 해당 query에서의 최솟값
        for i, (r, c) in enumerate(coords):
            matrix[r][c] = elements[i - 1] # 이전(시계 반대 방향) 칸의 원소를 입력
    
    return result
