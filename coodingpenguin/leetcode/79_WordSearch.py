class Solution:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def dfs(self, board, y, x, word):
        if len(word) == 0:
            return True
        if (
            (y < 0 or y >= len(board))
            or (x < 0 or x >= len(board[0]))
            or word[0] != board[y][x]
        ):
            return False
        current = board[y][x]
        board[y][x] = "#"
        result = False
        for dy, dx in self.directions:
            result = result or self.dfs(board, y + dy, x + dx, word[1:])
        board[y][x] = current
        return result

    def exist(self, board: List[List[str]], word: str) -> bool:
        for sy in range(len(board)):
            for sx in range(len(board[0])):
                if self.dfs(board, sy, sx, word):
                    return True
        return False
