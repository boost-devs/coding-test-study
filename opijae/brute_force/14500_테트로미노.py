import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr= []
for _ in range(n):
    arr.append(list(map(int, input().split())))

teris_blocks = [
    # ㅁㅁㅁㅁ 회전
    [(0,1),(0,2),(0,3)],
    [(1,0),(2,0),(3,0)],
    # ㅁㅁ
    # ㅁㅁ
    [(1,0),(0,1),(1,1)],
    # ㅁ
    # ㅁㅁㅁ 회전 및 뒤집기
    [(1,0),(2,0),(2,1)],
    [(1,0),(0,1),(0,2)],
    [(0,1),(1,1),(2,1)],
    [(0,1),(0,2),(-1,2)],
    [(0,1),(-1,1),(-2,1)],
    [(0,1),(1,0),(2,0)],
    [(1,0),(1,1),(1,2)], #
    [(0,1),(0,2),(1,2)],
    # ㅁㅁ
    #   ㅁㅁ 회전 및 뒤집기
    [(1,0),(1,1),(2,1)],
    [(0,1),(-1,1),(-1,2)],
    [(1,0),(1,-1),(2,-1)],
    [(0,1),(1,1),(1,2)],
    #   ㅁ
    # ㅁㅁㅁ 회전
    [(0,1),(0,2),(1,1)],
    [(0,1),(-1,1),(0,2)],
    [(1,0),(1,1),(2,0)],
    [(0,1),(-1,1),(1,1)]
]

_max = 0
for i in range(n):
    for j in range(m):
        # 매 좌표마다 모든 테트리스를 확인한다.
        for tetris in teris_blocks:
            _temp = arr[i][j]
            for cnt,(di,dj) in enumerate(tetris):
                if 0<=di+i<n and 0<=dj+j<m:
                    _temp += arr[di+i][dj+j]
                else:
                    break
            if cnt ==2:
                _max = max(_max,_temp)
print(_max)
