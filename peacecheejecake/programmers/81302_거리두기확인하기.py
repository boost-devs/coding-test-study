def search(place):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                for di, dj in directions:
                    # 맨해튼 거리가 1인 경우
                    ni, nj = i + di, j + dj
                    if ni < 0 or ni >= 5 or nj < 0 or nj >= 5: #5x5를 벗어난 경우
                        continue
                    elif place[ni][nj] == 'P':
                        return 0
                    
                    # 맨해튼 거리가 2인 경우
                    for ddi, ddj in directions:
                        nni, nnj = ni + ddi, nj + ddj
                        if (
                            nni == i and nnj == j
                            or nni < 0 or nni >= 5 or nnj < 0 or nnj >= 5
                        ): # 원래 응시자 자리로 돌아오거나, 5x5를 벗어난 경우
                            continue
                        elif place[nni][nnj] == 'P' and place[ni][nj] == 'O':
                            return 0
    return 1


def solution(places):
    return [search(place) for place in places]
