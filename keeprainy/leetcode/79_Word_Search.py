"""
#  LeetCode
#  ver.Python3
#
#  Created by GGlifer
#
#  Open Source
"""

from typing import *
from collections import deque


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # Brute Force by DFS

        dy = [-1, 0, 0, +1]
        dx = [0, -1, +1, 0]

        m = len(board)
        n = len(board[0])

        def is_valid(y: int, x: int) -> bool:
            return 0 <= y < m and 0 <= x < n

        is_visited = [[False for _ in range(n)] for _ in range(m)]

        def dfs(cy: int, cx: int, idx: int) -> bool:
            is_visited[cy][cx] = True

            if idx == len(word):
                return True

            for d in range(4):
                ny = cy + dy[d]
                nx = cx + dx[d]
                if is_valid(ny, nx) and not is_visited[ny][nx]:
                    if board[ny][nx] == word[idx]:
                        if dfs(ny, nx, idx+1):
                            return True

            is_visited[cy][cx] = False
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 1):
                        return True

        return False


def main():
    solution = Solution()


if __name__ == '__main__':
    main()
