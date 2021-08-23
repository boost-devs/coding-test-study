import sys

input = sys.stdin.readline

def get_total_dirt(r, c, t, arr):
    pass

r, c, t = map(int, input().split())  # 격자판 세로, 가로, 시간
arr = [list(map(int, input().split())) for _ in range(r)]  # 격자판 정보

print(get_total_dirt(r, c, t, arr))