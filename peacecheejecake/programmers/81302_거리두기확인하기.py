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

# ### 📌 푼 문제들

# - [거리두기 확인하기](https://programmers.co.kr/learn/courses/30/lessons/81302)
# - [수식 최대화](https://programmers.co.kr/learn/courses/30/lessons/67257#)
# - [튜플](https://programmers.co.kr/learn/courses/30/lessons/64065)

# ---

# ### 📝 간단한 풀이 과정

# #### 거리두기 확인하기

# - 모든 자리를 검사하면서, 응시자가 있는 경우 아래 순서로 검사합니다.
#   - 바로 옆 칸(맨해튼 거리=1)

# #### 문제 2 

# - 풀이과정

# #### 문제 3

# - 풀이과정

# ---

# ### 🙌 궁금한 점

# - 궁금한 점이 있을 경우 적어주시고 없을 경우 지워주세요.

# ---
