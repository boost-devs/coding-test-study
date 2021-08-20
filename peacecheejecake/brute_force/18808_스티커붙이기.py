# https://www.acmicpc.net/problem/18808
# 29200 KB / 824 ms


def add_sticker(board, sticker, si, sj):
    r, c = len(sticker), len(sticker[0])
    result = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            elm_add = board[si + i][sj + j] + sticker[i][j]
            if elm_add > 1:
                return
            result[i][j] = elm_add
    return result


def rotate(sticker):
    n, m = len(sticker), len(sticker[0])
    rotated = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            rotated[i][j] = sticker[n - j - 1][i]
    return rotated


def patch(board, replace, si, sj):
    r, c = len(replace), len(replace[0])
    for i in range(r):
        for j in range(c):
            board[si + i][sj + j] = replace[i][j]


def try_to_patch(board, sticker):
    r, c = len(sticker), len(sticker[0])
    for _ in range(4):
        is_valid_size = True
        for si in range(N - r + 1):
            if not is_valid_size:
                break
            
            for sj in range(M - c + 1):
                if r > N or c > M:
                    is_valid_size = False
                    break
                
                temp = add_sticker(board, sticker, si, sj)
                if temp is not None:
                    patch(board, temp, si, sj)           
                    return
                    
        sticker = rotate(sticker)
        r, c = c, r


if __name__ == '__main__':
    N, M, K = map(int, input().split())
    board = [[0] * M for _ in range(N)]
    for _ in range(K):
        r, _ = map(int, input().split())
        sticker = [list(map(int, input().split())) for _ in range(r)]
        try_to_patch(board, sticker)
        
    print(sum(map(sum, board)))
