def solution(rows, columns, queries):
    answer = []
    # 초기 행렬 초기화
    mat = []
    cnt = 0
    for _ in range(rows):
        temp = []
        for _ in range(columns):
            cnt += 1
            temp.append(cnt)
        mat.append(temp)

    for si,sj,ei,ej in queries:
        # index 맞춰주기위해 1씩 빼줌
        si -= 1
        sj -= 1
        ei -= 1
        ej -= 1
        w = ej - sj
        h = ei - si
        # 다음 좌표의 방향
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        idx = 0
        # 돌려야하는 배열? 직사각형 테두리의 꼭짓점들
        corners = [w, w + h, 2 * w + h]
        # 초기값 세팅
        prev = mat[si][sj] # si, sj가 시작점
        mat[si][sj] = mat[si+1][sj] # si, sj에는 바로 밑에 값이 들어감
        _min = prev # 최소 값 설정

        for i in range((w + h) * 2 - 1):
            # 코너에 도달했으면 방향 바꿔주기
            if i in corners:
                idx += 1
            # 새 좌표
            ni, nj = si + directions[idx][0], sj + directions[idx][1]
            temp = mat[ni][nj]
            mat[ni][nj] = prev
            prev = temp
            si, sj = ni,nj
            _min = min(_min,prev)
        answer.append(_min)
    return answer